CREATE DATABASE BankingFraudAnalysis;
USE BankingFraudAnalysis;

CREATE TABLE bank_transactions (
    transaction_id INT PRIMARY KEY,
    transaction_amount DECIMAL(10,2),
    location VARCHAR(100),
    merchant VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    fraud_label INT
);

SELECT COUNT(*) AS Total_Transactions
FROM bank_transactions;

## total fraud transactions
SELECT COUNT(*) AS Fraud_Transactions
FROM bank_transactions
WHERE fraud_label = 1;

## Total non fraud transactions
SELECT COUNT(*) AS Non_Fraud_Transactions
FROM bank_transactions
WHERE fraud_label = 0;

## Average transaction amount
SELECT ROUND(AVG(transaction_amount), 2) AS Average_Transaction
FROM bank_transactions;

## maximum transaction amount
SELECT MAX(transaction_amount) AS Highest_Transaction
FROM bank_transactions;

## minimum transaction amount
SELECT MAX(transaction_amount) AS Highest_Transaction
FROM bank_transactions;

## Fraud count by merchant
SELECT merchant,
       COUNT(*) AS Fraud_Count
FROM bank_transactions
WHERE fraud_label = 1
GROUP BY merchant
ORDER BY Fraud_Count DESC;

## Fraud count by location
SELECT location,
       COUNT(*) AS Fraud_Count
FROM bank_transactions
WHERE fraud_label = 1
GROUP BY location
ORDER BY Fraud_Count DESC;

## Fraud by Gender
SELECT gender,
       COUNT(*) AS Fraud_Count
FROM bank_transactions
WHERE fraud_label = 1
GROUP BY gender;

## Average transaction amoount by merchant
SELECT merchant,
       ROUND(AVG(transaction_amount),2) AS Avg_Amount
FROM bank_transactions
GROUP BY merchant
ORDER BY Avg_Amount DESC;