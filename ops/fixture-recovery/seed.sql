BEGIN;
SET LOCAL ROLE rafiq_api;
SELECT set_config('rafiq.fixture_owner', 'driver-a', true);
INSERT INTO rafiq_fixture.fixtures (owner_id) VALUES ('driver-a');
SELECT set_config('rafiq.fixture_owner', 'driver-b', true);
INSERT INTO rafiq_fixture.fixtures (owner_id) VALUES ('driver-b');
COMMIT;

-- Give Driver B a terminal prior job while preserving Driver A's queued job.
BEGIN;
SELECT id AS completed_id FROM rafiq_fixture.fixtures WHERE owner_id = 'driver-b' \gset
SET LOCAL ROLE rafiq_worker;
UPDATE rafiq_fixture.fixtures
SET status = 'running', generation = 1, lease_until = clock_timestamp() + interval '30 seconds'
WHERE id = :'completed_id';
UPDATE rafiq_fixture.fixtures
SET status = 'completed', lease_until = NULL,
    result = '{"version":1,"method":"synthetic-mean-v1","count":3,"mean":4}'
WHERE id = :'completed_id';
COMMIT;
