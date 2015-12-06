#!/usr/bin/env python
# coding:UTF-8
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os
import logging
import model.registerModel
import model.showModel
import model.initModel
import model.showDetailModel
import view.pokemonView
import view.mainView
import view.adminView
import view.detailView
import view.registerView
import dataObject
from google.appengine.ext import ndb

### HTML
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
	template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))
### HTML end

class MainHandler(BaseHandler):
    def get(self):
        # クライアント側から値を取り、オブジェクトにセットします
        ### 初期画面なので何も値を取ってきません
        
        # モデルで値を処理します
        mainViewInfo = dataObject.MainViewInfo()
        showModel = model.showModel.ShowModel(mainViewInfo)
        mainViewInfo = showModel.show()
        
        # 処理した値をビューに渡します
        mainView = view.mainView.MainView(mainViewInfo)
        values = mainView.getValues()
        
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
        self.render('main.html', values)        


class RegisterHandler(BaseHandler):
    def get(self):
        # クライアント側から値を取り、オブジェクトにセットします
        ### 初期画面なので何も値を取ってきません
        
        # モデルで値を処理します
        showDetailModel = model.showDetailModel.ShowDetailModel()
        registerViewInfo = showDetailModel.show()
        
        # 処理した値をビューに渡します
        registerView = view.registerView.RegisterView(registerViewInfo)
        values = registerView.getValues()
        
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
        self.render('register.html', values)        
        
        
    def post(self):
        # クライアント側から値を取り、オブジェクトにセットします
        updateInfo = dataObject.UpdateInfo(pokemon=self.request.get('pokemon'), team=self.request.get('team'))
        
        # モデルで値を処理します
        registerModel = model.registerModel.RegisterModel(updateInfo)
        updateInfo = registerModel.register()
        
        # 処理した値をビューに渡します
        pokemonView = view.pokemonView.PokemonView(updateInfo)
        values = pokemonView.getValues()
        
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
        self.render('register.html', values)


class AdminHandler(BaseHandler):
    def get(self):
        # クライアント側から値を取り、オブジェクトにセットします
        ### 初期画面なので何も値を取ってきません
        
        # モデルで値を処理します
        ### 初期画面なので何もしません
        
        # 処理した値をビューに渡します
        ### 初期画面なので何もしませんが、一応valuesを空で用意しておきます     
        values = {}
                
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
        self.render('admin.html', values)

    
    def post(self):
        # クライアント側から値を取り、オブジェクトにセットします
        ### 今回は特例的にpasswordをStringで取得するだけにします
        initPass = self.request.get('initPass') 
        
        if initPass == INITPASS:
            # モデルで値を処理します
            initModel = model.initModel.InitModel()
            initFlag = initModel.init()
            
            # 処理した値をビューに渡します
            ### 今回は特例的にinitFlagというBooleanを渡すだけにします
            adminView = view.adminView.AdminView(initFlag)
            values = adminView.getValues()

        else:
            logging.warning(u"DB初期化パスワードが違います")                    
            # モデルで値を処理します
            ### 処理はありません
            
            # 処理した値をビューに渡します
            errorView = view.adminView.ErrorView()
            values = errorView.getValues()
            
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
            self.render('admin.html', values)
        

class DetailHandler(BaseHandler):
    def get(self):
        # クライアント側から値を取り、オブジェクトにセットします
        ### 初期画面なので何も値を取ってきません

        # モデルで値を処理します
        showDetailModel = model.showDetailModel.ShowDetailModel()
        detailViewInfo = showDetailModel.show()
        
        # 処理した値をビューに渡します
        detailView = view.detailView.DetailView(detailViewInfo)
        values = detailView.getValues()
        
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
        self.render('detail.html', values)        


class RuleHandler(BaseHandler):
    def get(self):
        # クライアント側から値を取り、オブジェクトにセットします
        ### 初期画面なので何も値を取ってきません
        
        # モデルで値を処理します
        ### 何もしません
        
        # 処理した値をビューに渡します
        ### 何もしません
        values = {}
                        
        # ビューで作られた値をhtmlにセットします
        ### self.render('xxxx.html', values)の形式を守って書きます
        self.render('rule.html', values)        



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler),
    ('/admin', AdminHandler),
    ('/detail', DetailHandler),
    ('/rule', RuleHandler)
], debug=True)

INITPASS = 'neat-nimbus'
