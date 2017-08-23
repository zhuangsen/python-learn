# -*- coding: utf-8 -*-
# import web
# import MySQLdb
# import MySQLdb.cursors

import web
import pymysql
import pymysql.cursors

render = web.core.template.render('templates')

urls = (
    '/article', 'article',
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)
app = web.application(urls, globals())


class index:
    def GET(self):
        query = web.input()
        print(query)
        return web.seeother('/article')


class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        return web.ctx.env


class hello:
    def GET(self, name):
        return render.index(name)


class article:
    def GET(self):
        conn = pymysql.connect(host='localhost', user='root', passwd='inserthome', db='test', port=3306,
                               cursorclass=pymysql.cursors.DictCursor)
        cur = conn.cursor()
        cur.execute('select * from article')
        r = cur.fetchall()
        cur.close()
        conn.close()
        print(r)
        return render.article(r)


if __name__ == '__main__':
    app.run()
