REVOKE ALL ON DATABASE rafiq FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM PUBLIC;

CREATE ROLE rafiq_migrate LOGIN PASSWORD 'local-migration-only';
CREATE ROLE rafiq_api LOGIN PASSWORD 'local-api-only';
CREATE ROLE rafiq_worker LOGIN PASSWORD 'local-worker-only';

GRANT CONNECT ON DATABASE rafiq TO rafiq_migrate, rafiq_api, rafiq_worker;
CREATE SCHEMA rafiq_fixture AUTHORIZATION rafiq_migrate;
GRANT USAGE ON SCHEMA rafiq_fixture TO rafiq_api, rafiq_worker;
