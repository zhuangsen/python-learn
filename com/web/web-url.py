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
        return 'index method'


class blog:
    def GET(self):
        return 'blog method'

    def POST(self):
        return 'blog post method'


class hello:
    def GET(self, name):
        return 'hello,' + name


if __name__ == '__main__':
    app.run()
