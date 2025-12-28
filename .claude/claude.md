# Blog Workflow

## Adding a New Blog Post

1. Create notebook in appropriate folder under `nbs/` (e.g., `nbs/Interview-prep/02_Post_Name.ipynb`)
2. Add entry to `nbs/sidebar.yml`
3. Preview locally:
   ```
   conda activate apps
   nbdev_docs && nbdev_clean && nbdev_prepare && nbdev_preview
   ```
4. Verify at the localhost URL shown in terminal

## Pushing Changes

```
git add .
git commit -m ':sparkles: new blog on <topic>'
git push
```

## References

See [maintaining.md](../maintaining.md) for:
- First-time setup instructions
- Deploying under subdomain
- Theme and styling tips
- Disabling notebook execution

