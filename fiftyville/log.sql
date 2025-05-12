-- Search for crime scene reports by date and location
SELECT description
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28;

-- Search for interview transcripts mentioning a bakery
SELECT transcription
FROM interviews
WHERE year = 2021
AND month = 7
AND day = 28
AND transcript LIKE '%bakery%';

-- Find activities and people at the bakery within a specific time
SELECT bakery_security_logs.activity,
       bakery_security_logs.license_plate,
       people.name
FROM people
JOIN bakery_security_logs
ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.year = 2021
AND bakery_security_logs.month = 7
AND bakery_security_logs.day = 28
AND bakery_security_logs.hour = 10
AND bakery_security_logs.minute BETWEEN 15 AND 25;

-- Identify people making withdrawals from a specific ATM
SELECT people.name, atm_transactions.transaction_type
FROM people
JOIN bank_accounts
ON bank_accounts.person_id = people.id
JOIN atm_transactions
ON atm_transactions.account_number = bank_accounts.account_number
WHERE atm_transactions.year = 2021
AND atm_transactions.month = 7
AND atm_transactions.day = 28
AND atm_location = 'Legett Street'
AND atm_transactions.transaction_type = 'withdraw';

-- Add caller and receiver names to the phone_calls table
UPDATE phone_calls
SET caller_name = (SELECT name FROM people WHERE people.phone_number = phone_calls.caller);

UPDATE phone_calls
SET receiver_name = (SELECT name FROM people WHERE people.phone_number = phone_calls.receiver);

-- List short phone calls on a specific day
SELECT caller, caller_name, receiver, receiver_name
FROM phone_calls
WHERE year = 2021
AND month = 7
AND day = 28
AND duration < 60;

-- Update flight origins and destinations with city names
UPDATE flights
SET origin_airport_id = (SELECT city FROM airports WHERE airports.id = flights.origin_airport_id);

UPDATE flights
SET destination_airport_id = (SELECT city FROM airports WHERE airports.id = flights.destination_airport_id);

-- Find the earliest flight on a specific day
SELECT id, hour, minute, origin_airport_id, destination_airport_id
FROM flights
WHERE year = 2021
AND month = 7
AND day = 29
ORDER BY hour ASC, minute ASC
LIMIT 1;

-- Find passengers on a specific flight
SELECT flights.destination_airport_id, people.name, people.phone_number, people.license_plate
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON flights.id = passengers.flight_id
WHERE flights.id = 36
ORDER BY flights.hour ASC;

-- Combine data to identify a specific person
SELECT name
FROM people
JOIN passengers
ON people.passport_number = passengers.passport_number
JOIN flights
ON flights.id = passengers.flight_id
WHERE flights.year = 2021
AND flights.month = 7
AND flights.day = 29
AND flights.id = 36
AND name IN (
    SELECT phone_calls.caller_name
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60
)
AND name IN (
    SELECT people.name
    FROM people
    JOIN bank_accounts
    ON bank_accounts.person_id = people.id
    JOIN atm_transactions
    ON atm_transactions.account_number = bank_accounts.account_number
    WHERE atm_transactions.year = 2021
    AND atm_transactions.month = 7
    AND atm_transactions.day = 28
    AND atm_location = 'Legett Street'
    AND atm_transactions.transaction_type = 'withdraw'
)
AND name IN (
    SELECT people.name
    FROM people
    JOIN bakery_security_logs
    ON bakery_security_logs.license_plate = people.license_plate
    WHERE bakery_security_logs.year = 2021
    AND bakery_security_logs.month = 7
    AND bakery_security_logs.day = 28
    AND bakery_security_logs.hour = 10
    AND bakery_security_logs.minute BETWEEN 15 AND 25
);
