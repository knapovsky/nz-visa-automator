#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://onlineservices.immigration.govt.nz/
# https://onlineservices.immigration.govt.nz/WorkingHoliday/Application/Create.aspx?CountryId=57

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

def select_option_old(driver, item_name, select_el_id, option_string):
    print('S->' + item_name)
    driver.execute_script("$('#"+ select_el_id +"').css('display', 'block');")
    select = driver.find_element_by_id(select_el_id)
    for option in select.find_elements_by_tag_name('option'):
        if option.text == option_string:
            option.click() # select() in earlier versions of webdriver
            break

def select_option(driver, item_name, option_id, option_string):
    print('S->' + item_name)
    driver.execute_script("$('#"+ option_id +"').css('display', 'block');")
    select = Select(browser.find_element_by_id(option_id))
    select.select_by_visible_text(option_string)

def input_option(driver, item_name, option_id, option_string):
    print('I->' + item_name)
    option = driver.find_element_by_id(option_id)
    option.clear()
    option.send_keys(option_string)

def checkbox_option(driver, item_name, option_id, option):
    print('C->' + item_name)
    driver.execute_script("$('#"+ option_id +"').css('display', 'block');")
    checkbox = driver.find_element_by_id(option_id)
    checkbox.click()

browser = webdriver.Firefox()
browser.get('https://onlineservices.immigration.govt.nz/?WHS')

quit()
## BLOCK1
## Personal Details
## ----------------
### Personal Detail
input_option(browser, 'Family Name', 'ContentPlaceHolder1_personDetails_familyNameTextBox', 'John')
input_option(browser, 'Given Name', 'ContentPlaceHolder1_personDetails_givenName1Textbox', 'Doe')
select_option(browser, 'Title', 'ContentPlaceHolder1_personDetails_titleDropDownList', 'Other')
input_option(browser, 'Other title', 'ContentPlaceHolder1_personDetails_otherTitleTextBox', 'Ing.')
select_option(browser, 'Gender', 'ContentPlaceHolder1_personDetails_genderDropDownList', 'Male')
input_option(browser, 'Date of birth', 'ContentPlaceHolder1_personDetails_dateOfBirthDatePicker_DatePicker', '10 December, 1991')
select_option(browser, 'Country of birth', 'ContentPlaceHolder1_personDetails_CountryDropDownList', 'Australia')
### Address
input_option(browser, 'Street Number', 'ContentPlaceHolder1_addressContactDetails_address_streetNumberTextbox', '65')
input_option(browser, 'Street Name', 'ContentPlaceHolder1_addressContactDetails_address_address1TextBox', 'Street Address')
input_option(browser, 'Suburb', 'ContentPlaceHolder1_addressContactDetails_address_suburbTextBox', 'Street Address')
input_option(browser, 'City', 'ContentPlaceHolder1_addressContactDetails_address_cityTextBox', 'City')
input_option(browser, 'Province', 'ContentPlaceHolder1_addressContactDetails_address_provinceStateTextBox', 'Country')
input_option(browser, 'ZIP', 'ContentPlaceHolder1_addressContactDetails_address_postalCodeTextBox', '66666')
select_option(browser, 'Country', 'ContentPlaceHolder1_addressContactDetails_address_countryDropDownList', 'Country')
### Contact Details
input_option(browser, 'Phone number', 'ContentPlaceHolder1_addressContactDetails_contactDetails_phoneNumberMobileTextBox', '420 420 420420')
input_option(browser, 'E-Mail', 'ContentPlaceHolder1_addressContactDetails_contactDetails_emailAddressTextBox', 'john@doe.com')
select_option(browser, 'Agent', 'ContentPlaceHolder1_hasAgent_representedByAgentDropdownlist', 'No')
select_option(browser, 'Communication Method', 'ContentPlaceHolder1_communicationMethod_communicationMethodDropDownList', 'Email')
select_option(browser, 'Has Credit Card', 'ContentPlaceHolder1_hasCreditCard_hasCreditCardDropDownlist', 'Yes')

## BLOCK2
## Identification
## --------------
### Passport
input_option(browser, 'Passport Number', 'ContentPlaceHolder1_identification_passportNumberTextBox', '66666666')
input_option(browser, 'Passport Number Confirmation', 'ContentPlaceHolder1_identification_confirmPassportNumberTextBox', '66666666')
input_option(browser, 'Passport Expiry Date', 'ContentPlaceHolder1_identification_passportExpiryDateDatePicker_DatePicker', '24 December, 2030')
### Second ID
### ID: 204825460, 4.5.2015, 4.5.2025
#TODO select_option(browser, 'Second ID Type', 'ContentPlaceHolder1_identification_otherIdentificationDropdownlist', 'National ID')
input_option(browser, 'Second ID Issue Date', 'ContentPlaceHolder1_identification_otherIssueDateDatePicker_DatePicker', '30 May, 2022')
input_option(browser, 'Second ID Expiry Date', 'ContentPlaceHolder1_identification_otherExpiryDateDatePicker_DatePicker', '30 May, 2027')

## BLOCK3
### Occupation Details
# L783300 Computer Maintenance Services || P921000 Libraries
# 263111 Computer Network and Systems Engineer

## BLOCK4
# HEALTH
# ------
select_option(browser, 'Dialysis', 'ContentPlaceHolder1_medicalConditions_renalDialysisDropDownList', 'No')
select_option(browser, 'Tuberculosis', 'ContentPlaceHolder1_medicalConditions_tuberculosisDropDownList', 'No')
select_option(browser, 'Cancer', 'ContentPlaceHolder1_medicalConditions_cancerDropDownList', 'No')
select_option(browser, 'Heart Disease', 'ContentPlaceHolder1_medicalConditions_heartDiseaseDropDownList', 'No')
select_option(browser, 'Disability', 'ContentPlaceHolder1_medicalConditions_disabilityDropDownList', 'No')
select_option(browser, 'Hospitalisation', 'ContentPlaceHolder1_medicalConditions_hospitalisationDropDownList', 'No')
select_option(browser, 'Residental Care', 'ContentPlaceHolder1_medicalConditions_residentailCareDropDownList', 'No')
select_option(browser, 'Tuberculosis Risk', 'ContentPlaceHolder1_medicalConditions_tbRiskDropDownList', 'No')

# BLOCK5
# CHARACTER
# ---------
select_option(browser, 'Imprisonment 5 Years', 'ContentPlaceHolder1_character_imprisonment5YearsDropDownList', 'No')
select_option(browser, 'Imprisonment 12 Months', 'ContentPlaceHolder1_character_imprisonment12MonthsDropDownList', 'No')
select_option(browser, 'Removal Order', 'ContentPlaceHolder1_character_removalOrderDropDownList', 'No')
select_option(browser, 'Deportation', 'ContentPlaceHolder1_character_deportedDropDownList', 'No')
select_option(browser, 'Charged', 'ContentPlaceHolder1_character_chargedDropDownList', 'No')
select_option(browser, 'Convicted', 'ContentPlaceHolder1_character_convictedDropDownList', 'No')
select_option(browser, 'Under investigation', 'ContentPlaceHolder1_character_underInvestigationDropDownList', 'No')
select_option(browser, 'Excluded or refused', 'ContentPlaceHolder1_character_excludedDropDownList', 'No')
select_option(browser, 'Removed', 'ContentPlaceHolder1_character_removedDropDownList', 'No')

# BLOCK6
# WHS
# ---
select_option(browser, 'Previous Visa', 'ContentPlaceHolder1_offshoreDetails_commonWHSQuestions_previousWhsPermitVisaDropDownList', 'No')
select_option(browser, 'Sufficient Funds', 'ContentPlaceHolder1_offshoreDetails_commonWHSQuestions_sufficientFundsHolidayDropDownList', 'Yes')
input_option(browser, 'Entry date', 'ContentPlaceHolder1_identification_passportExpiryDateDatePicker_DatePicker', '1 January, 2019')
#TODO ! Change ID select_option(browser, 'NZ Before', 'ContentPlaceHolder1_offshoreDetails_commonWHSQuestions_previousWhsPermitVisaDropDownList', 'No')
select_option(browser, 'Sufficient Funds for Outward Ticked', 'ContentPlaceHolder1_offshoreDetails_requirementsQuestions_sufficientFundsOnwardTicketDropDownList', 'Yes')
select_option(browser, 'Meet requirement', 'ContentPlaceHolder1_offshoreDetails_requirementsQuestions_readRequirementsDropDownList', 'Yes')

# BLOCK7
# SUBMIT
# ------
checkbox_option(browser, 'I understand false statements', 'ContentPlaceHolder1_falseStatementCheckBox', 'Yes')
checkbox_option(browser, 'I understand notes', 'ContentPlaceHolder1_notesCheckBox', 'Yes')
checkbox_option(browser, 'I understand obligations', 'ContentPlaceHolder1_circumstancesCheckBox', 'Yes')
checkbox_option(browser, 'I declare warrants', 'ContentPlaceHolder1_warrantsCheckBox', 'Yes')
checkbox_option(browser, 'I authorize enquiries', 'ContentPlaceHolder1_informationCheckBox', 'Yes')
checkbox_option(browser, 'I authorize health check', 'ContentPlaceHolder1_healthCheckBox', 'Yes')
checkbox_option(browser, 'I accept advice', 'ContentPlaceHolder1_adviceCheckBox', 'Yes')
checkbox_option(browser, 'I understand registration law', 'ContentPlaceHolder1_registrationCheckBox', 'Yes')
checkbox_option(browser, 'I understand entitlement', 'ContentPlaceHolder1_entitlementCheckbox', 'Yes')
checkbox_option(browser, 'I am responsible', 'ContentPlaceHolder1_permitExpiryCheckBox', 'Yes')
checkbox_option(browser, 'I am fully aware', 'ContentPlaceHolder1_medicalInsuranceCheckBox', 'Yes')