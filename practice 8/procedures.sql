
-- Insert contact

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_name
    ) THEN
        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_name;
    ELSE
        INSERT INTO contacts(first_name, phone)
        VALUES(p_name, p_phone);
    END IF;
END;
$$;


-- Insert many contacts with validation

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(
    p_names TEXT[],
    p_phones TEXT[],
    INOUT p_invalid_data TEXT[] DEFAULT ARRAY[]::TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
BEGIN
    p_invalid_data := ARRAY[]::TEXT[];

    IF array_length(p_names, 1) IS DISTINCT FROM
       array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Names and phones must have equal lengths';
    END IF;

    FOR i IN 1..COALESCE(array_length(p_names, 1), 0)
    LOOP
        IF p_names[i] IS NULL OR
           p_names[i] = '' OR
           p_phones[i] IS NULL OR
           p_phones[i] !~ '^\+?[0-9]{7,15}$' THEN

            p_invalid_data := array_append(
                p_invalid_data,
                COALESCE(p_names[i], 'NULL') || ' - ' ||
                COALESCE(p_phones[i], 'NULL')
            );

        ELSE
            IF EXISTS (
                SELECT 1
                FROM contacts
                WHERE first_name = p_names[i]
            ) THEN
                UPDATE contacts
                SET phone = p_phones[i]
                WHERE first_name = p_names[i];
            ELSE
                INSERT INTO contacts(first_name, phone)
                VALUES(p_names[i], p_phones[i]);
            END IF;
        END IF;
    END LOOP;
END;
$$;


-- 3. Delete contact by name or phone

CREATE OR REPLACE PROCEDURE delete_contact(
    p_name VARCHAR DEFAULT NULL,
    p_phone VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF p_name IS NULL AND p_phone IS NULL THEN
        RAISE EXCEPTION 'Enter name or phone';
    END IF;

    DELETE FROM contacts
    WHERE (p_name IS NOT NULL AND first_name = p_name)
       OR (p_phone IS NOT NULL AND phone = p_phone);
END;
$$;
