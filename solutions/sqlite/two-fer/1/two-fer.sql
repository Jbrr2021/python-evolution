-- Atualiza todos os registros da tabela twofer
UPDATE twofer

-- Define o valor da coluna response
SET response = CASE

    -- Quando input estiver vazio, usamos "you"
    WHEN input = '' THEN 'One for you, one for me.'

    -- Quando input tiver um nome, usamos esse nome na frase
    ELSE 'One for ' || input || ', one for me.'

END;
