git pull origin home       # make sure home branch is up to date
git checkout home          # switch to home branch
# make changes
git add .
git commit -m "Work from home"
git push origin home       # push home work

#  merge changes

git checkout main
git merge office      # merge office changes
git merge home        # merge home changes
git push origin main
