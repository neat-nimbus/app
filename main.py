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
import model.registerModel
import model.showModel
import view.pokemonView
import view.mainView
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
        ### 初期画面なので何もしません
        
        # 処理した値をビューに渡します
        ### 初期画面なので何もしませんが、一応valuesを空で用意しておきます     
        values = {}
                
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

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/register', RegisterHandler)
], debug=True)
