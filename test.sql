CREATE TABLE new_job (
    jobid INTEGER PRIMARY KEY AUTOINCREMENT,
    name_of_organization TEXT,
    phone_number TEXT,
    location TEXT,
    salary REAL,
    emailid TEXT
);
-- INSERT INTO new_jobs (name_of_organization, phone_number, location, salary, emailid)
-- SELECT name_of_organization, phone_number, location, salary, emailid FROM beautician;

-- DROP TABLE jobs;

-- ALTER TABLE new_jobs RENAME TO jobs;
