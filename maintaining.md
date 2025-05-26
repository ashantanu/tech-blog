# how to maintain this?

## First time setup
Basic Setup (only first time)
```
git clone https://github.com/ashantanu/tech-blog.git
conda install -c conda-forge -y jupyterlab
conda install -c fastai -y nbdev
nbdev_install_quarto
pip install jupyterlab-quarto
nbdev_install_hooks
```

building notebooks (only first time?)
```
nbdev_export
pip install -e '.[dev]'
```

Also need to follow [this](https://nbdev.fast.ai/migrating.html#edit-workflow-permissions) due to migration to new verison 

## make changes
```
conda activate apps
nbdev_docs
nbdev_clean
nbdev_prepare
nbdev_preview
```

Push to github to deploy
```
git add .
git commit -m ':sparkes: new blog on claude'
git push
```

## deploying under subdomain
create subdomain record in wix
https://support.wix.com/en/article/connecting-a-subdomain-to-an-external-resource

add it to githubpages
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain

final step is a bit confusing, but it is https://github.com/ashantanu/tech-blog/settings/pages
Custom Domain > add subdomain > save


# other tips
comments with : https://quarto.org/docs/reference/projects/websites.html#giscus
disable notebook execution with : a raw cell at top with below
best alternative themes: lux, darkly ( goes in _quatro.yml>format>html>theme)
change highlighting: https://quarto.org/docs/output-formats/html-code#highlighting
```
---
skip_exec: true
skip_showdoc: true
---
```