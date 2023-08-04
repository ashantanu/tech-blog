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
nbdev_install_hooks
nbdev_prepare
nbdev_docs
nbdev_preview
```

Push to github to deploy
```
git add .
git commit -m ':bug: fix'
git push
```

## deploying under subdomain
create subdomain record in wix
https://support.wix.com/en/article/connecting-a-subdomain-to-an-external-resource

add it to githubpages
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain

final step is a bit confusing, but it is https://github.com/ashantanu/tech-blog/settings/pages
Custom Domain > add subdomain > save