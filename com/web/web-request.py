# -*- coding: utf-8 -*-
import web

urls = (
    '/index', 'index',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)
app = web.application(urls, globals())


class index:
    def GET(self):
        query = web.input()
        return query


class blog:
    def POST(self):
        data = web.input()
        return data

    def GET(self):
        return web.ctx.env

class hello:
    def GET(self, name):
        return open(r'index.html').read()


if __name__ == '__main__':
    app.run()
