CREATE TABLE IF NOT EXISTS measurements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    experiment_id TEXT NOT NULL,
    timestamp TEXT NOT NULL,
    metric TEXT NOT NULL,
    value REAL NOT NULL,
    unit TEXT NOT NULL,
    source TEXT NOT NULL,
    target TEXT
);

CREATE INDEX IF NOT EXISTS idx_measurements_experiment
ON measurements(experiment_id);

CREATE INDEX IF NOT EXISTS idx_measurements_timestamp
ON measurements(timestamp);
