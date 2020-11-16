# MCSS Redis App

![Deploy to GCP](https://github.com/fujitsueos/mcss-redis-app/workflows/Deploy%20to%20GCP/badge.svg)

Test application that uses GCP App Engine and Redis. On a GitHub new tag release (`v*`), source code (`scr` folder) is pushed to GCP bucket by using [setup-gcloud](https://github.com/google-github-actions/setup-gcloud) and [upload-cloud-storage](https://github.com/google-github-actions/upload-cloud-storage) GitHub actions.
