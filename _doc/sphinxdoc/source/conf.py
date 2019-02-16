# -*- coding: utf-8 -*-
import sys
import os
import sphinx_rtd_theme
from pyquickhelper.helpgen.default_conf import set_sphinx_variables, get_default_stylesheet


sys.path.insert(0, os.path.abspath(os.path.join(os.path.split(__file__)[0])))

local_template = os.path.join(os.path.abspath(
    os.path.dirname(__file__)), "phdoc_templates")

set_sphinx_variables(__file__, "mlinsights", "Xavier Dupré", 2019,
                     "sphinx_rtd_theme", [
                         sphinx_rtd_theme.get_html_theme_path()],
                     locals(), extlinks=dict(
                         issue=('https://github.com/sdpython/mlinsights/issues/%s', 'issue')),
                     title="mlinsights", book=True)

blog_root = "http://www.xavierdupre.fr/app/mlinsights/helpsphinx/"

html_context = {
    'css_files': get_default_stylesheet() + ['_static/my-styles.css'],
}

html_logo = "project_ico.png"

html_sidebars = {}

language = "en"

mathdef_link_only = True

epkg_dictionary.update({
    'decision tree': 'https://en.wikipedia.org/wiki/Decision_tree',
    'DOT': 'https://en.wikipedia.org/wiki/DOT_(graph_description_language)',
    'Iris': 'http://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html',
    'L1': 'https://en.wikipedia.org/wiki/Norm_(mathematics)#Absolute-value_norm',
    'L2': 'https://en.wikipedia.org/wiki/Norm_(mathematics)#Euclidean_norm',
    'keras': 'https://keras.io/',
    'MLPClassifier': 'http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html',
    'MLPRegressor': 'http://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPRegressor.html',
    'pandas': ('http://pandas.pydata.org/pandas-docs/stable/',
               ('http://pandas.pydata.org/pandas-docs/stable/generated/pandas.{0}.html', 1),
               ('http://pandas.pydata.org/pandas-docs/stable/generated/pandas.{0}.{1}.html', 2)),
    'PCA': 'https://en.wikipedia.org/wiki/Principal_component_analysis',
    'RandomForestRegressor': 'http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html',
    'REST API': 'https://en.wikipedia.org/wiki/Representational_state_transfer',
    'sklearn': ('http://scikit-learn.org/stable/',
                ('http://scikit-learn.org/stable/modules/generated/{0}.html', 1),
                ('http://scikit-learn.org/stable/modules/generated/{0}.{1}.html', 2)),
    't-SNE': 'https://lvdmaaten.github.io/tsne/',
    'TSNE': 'https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html',
})
