#!/usr/bin/bash
# Before executing do `export PULP3_HOST=host`
docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
    -i http://"${PULP3_HOST:-localhost}"/pulp/api/v3/docs/.json\?format\=openapi \
    -l python \
    -o /local \
    -c /local/config.json
