'''App Engine Deployment.'''


def GenerateConfig(context):
    '''Creates a App Engine.'''

    resources = []
    base_name = context.env['name']
    project = context.env['project']
    vpc_connector = f'projects/{ project }/locations/{ context.properties["gcpLocation"] }/connectors/{ context.properties["vpc_access_connector"] }'
    main_file = f'https://storage.googleapis.com/{ context.properties["bucket_name"] }/src/main.py'
    req_file = f'https://storage.googleapis.com/{ context.properties["bucket_name"] }/src/requirements.txt'
    html_file = f'https://storage.googleapis.com/{ context.properties["bucket_name"] }/src/index.html'

    app_engine = {
        'name': base_name,
        'type': 'gcp-types/appengine-v1:apps.services.versions',
        'properties': {
            'runtime': 'python38',
            'entrypoint': {
              'shell': 'gunicorn -b :8080 -w 2 main:app'
            },
            'servicesId': f'{ base_name }-service',
            'appsId': project,
            'deployment': {
              'files': {
                'main.py': {
                  'sourceUrl': main_file
                },
                'requirements.txt': {
                  'sourceUrl': req_file
                },
                'index.html': {
                  'sourceUrl': html_file
                }
              }
            },
            'envVariables': {
              'REDISHOST': context.properties['redishost'],
              'REDISPORT': context.properties['redisport'],
              'APP_NAME': base_name
            },
            'vpcAccessConnector': {
              'name': vpc_connector
            }
        }
    }

    resources.append(app_engine)

    return {'resources': resources}

