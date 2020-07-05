import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://selenium1py.pythonanywhere.com/ru/')

WebUI.click(findTestObject('Object Repository/Page_Oscar - Sandbox/a_'))

WebUI.setText(findTestObject('Object Repository/Page_    Oscar - Sandbox/input_  _registration-email'), 'user1234@gmail.com')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_    Oscar - Sandbox/input__registration-password1'), 'wL4+5HZrZPwK9gn+EibBEfoXSILmCm47')

WebUI.setEncryptedText(findTestObject('Object Repository/Page_    Oscar - Sandbox/input_ _registration-password2'), 'wL4+5HZrZPwK9gn+EibBEfoXSILmCm47')

WebUI.click(findTestObject('Object Repository/Page_    Oscar - Sandbox/button_'))

WebUI.click(findTestObject('Object Repository/Page_Oscar - Sandbox/div_'))

