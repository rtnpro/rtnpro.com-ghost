# -*- coding: utf8 -*-

import os

from nikola.plugin_categories import Task
from nikola import utils


class RenderHome(Task):
    """
    Render home page for www.rtnpro.com
    """
    name = "render_home"

    def gen_tasks(self):
        template_name = "home.tmpl"
        output_name = "index.html"

        context = {
            'msg': 'Hello world'
        }
        task = self.site.render_template(
            template_name, output_name, context)
        task['basename'] = 'render_home'
        task['uptodate'] = True
        task['clean'] = True

        yield task
