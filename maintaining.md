# how to maintain this?

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

make changes
```
nbdev_prepare
nbdev_preview
```

Push to github
```
git add .
git commit -m 'adding new doc' # Update this text with your own message
git push
```