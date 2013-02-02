# -*- coding: utf8 -*-
import os
from nikola.plugin_categories import Task
import json


class RenderHome(Task):
    """
    Render home page for www.rtnpro.com
    """
    name = "render_home"

    def gen_tasks(self):
        template_name = "home.tmpl"
        output_name = "output/index.html"
        f = open(os.path.join(os.path.split(__file__)[0], 'projects.json'))
        projects = json.load(f)
        f.close()
        context = {
            'lang': 'en',
            'title': '@rtnpro',
            'description': 'Welcome to @rtnpro\'s personal website.',
            'upstream_projects': projects['upstream'],
            'own_projects': projects['own']
        }
        context.update(self.site.config['GLOBAL_CONTEXT'])
        self.site.render_template(
            template_name, output_name, context)

        yield {
            'basename': 'render_home',
            'uptodate': [True],
            'clean': True,
            'actions': []
        }
