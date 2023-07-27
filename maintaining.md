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
nbdev_prepare
nbdev_docs
nbdev_preview
```

Push to github to deploy
```
git add .
git commit -m 'adding new doc' # Update this text with your own message
git push
```