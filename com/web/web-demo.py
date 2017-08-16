# -*- coding: utf-8 -*-
import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())


class hello:
    def GET(self, name):
        print(name)
        return open(r'webpy.html', 'r')


if __name__ == "__main__":
    app.run()
