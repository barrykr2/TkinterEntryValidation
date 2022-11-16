import tkinter as tk
import clsDates as dateLib
import clsStatusBar as status_bar
import clsStrings as stringLib
import clsErrors as errorLogger
from dataclasses import dataclass

# initialise the date class outside the individual classes so it maintains status between calls 
chkDate = dateLib.check_date(None, dateLib.nullDate)
chkDate.allowShortCutKeys = True
            
@dataclass
class dataObj:
    isValid: bool = False
    value: str = None
    widgetJustification: str = None
    toolTip: str = None

class validate:
    # This class is used by the GUI to do data type validation and formating.
    # (business logic will need to be elsewhere)
    # Return must always be of type "dataObj"
    
    def __init__(self, statusBarObj: dataObj = None, errorLogObj: errorLogger = None):
        self.statusBarObj = statusBarObj
        self.errorLogObj = errorLogObj
    
    # ------ Start of Data Type Validations ------
    def validate_decimal(self, value: str = None, decimal_places: int = 2):
        formatting = "{: ." + str(decimal_places) + "f}"
        tool_tip = 'Enter a number with ' + str(decimal_places) + ' decimal places.'
        returnObj = dataObj(isValid = False, value = formatting.format(0), widgetJustification = tk.RIGHT, toolTip = tool_tip)
        
        if value:
            try:
                returnObj = dataObj(isValid = True, value = formatting.format(float(value)), widgetJustification = returnObj.widgetJustification, toolTip = tool_tip)
            except Exception as e:
                pass
        
            self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: decimal(' + str(decimal_places) + '))')
        return returnObj
    
    def validate_float(self, value: str = None):
        tool_tip = 'Enter any number (type: float).'
        returnObj = dataObj(isValid = False, value = 0, widgetJustification = tk.RIGHT, toolTip = tool_tip)
        
        if value:
            try:
                returnObj = dataObj(isValid = True, value = float(value), widgetJustification = returnObj.widgetJustification, toolTip = tool_tip)
            except Exception as e:
                pass
        
            self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: float)')
        return returnObj
    
    def validate_integer(self, value: str = None):
        tool_tip = 'Enter a whole number (type: integer).'
        returnObj = dataObj(isValid = False, value = 0, widgetJustification = tk.RIGHT, toolTip = tool_tip)
        
        if value:
            try:
                returnObj = dataObj(isValid = True, value = int(value), widgetJustification = returnObj.widgetJustification, toolTip = tool_tip)
                self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: integer)')
            except Exception as e:
                tmpVal = self.validate_float(value)
                if tmpVal.isValid:
                    returnObj = dataObj(isValid = True, value = round(float(value)), widgetJustification = returnObj.widgetJustification, toolTip = tool_tip)
                    if float(value) > float(returnObj.value):
                        self.update_status_bar(True, 'Info: "' + str(value) + '" rounded down (type: integer)')
                    else:
                        self.update_status_bar(True, 'Info: "' + str(value) + '" rounded up (type: integer)')

                else:
                    self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: integer)')
        return returnObj
    
    def validate_Date(self, value: str = None):
        returnObj = dataObj(isValid = False, value = dateLib.nullDate, widgetJustification = tk.CENTER, toolTip = dateLib.toolTip)

        if value:
            try:
                chkDate.dateCheck(value)
                self.update_status_bar(not chkDate.isValid, chkDate.messages)                
                returnObj = dataObj(isValid = chkDate.isValid, value = chkDate.formattedDate, widgetJustification = returnObj.widgetJustification, toolTip = dateLib.toolTip)
            except Exception as e:
                pass
        
        return returnObj
    
    def validate_title(self, value = None):
        tool_tip = 'Enter text and it will be formated as a Title.'
        returnObj = dataObj(isValid = False, value = value, widgetJustification = tk.LEFT, toolTip = tool_tip)
        
        if value:
            try:
                strFmt = stringLib.string_format()
                returnObj = dataObj(isValid = True, value = strFmt.title(value), widgetJustification = returnObj.widgetJustification, toolTip = tool_tip)
            except Exception as e:
                pass
        
        return returnObj
    
    def validate_sentence(self, value = None):
        tool_tip = 'Enter text and it will be formated as a Sentence.'
        returnObj = dataObj(isValid = False, value = value, widgetJustification = tk.LEFT, toolTip = tool_tip)
        
        if value:
            try:
                strFmt = stringLib.string_format()
                returnObj = dataObj(isValid = True, value = strFmt.sentence(value), widgetJustification = returnObj.widgetJustification, toolTip = tool_tip)
            except Exception as e:
                pass
        
        return returnObj
    
    # ------ End of Data Type Validations ------
    
    def update_status_bar(self, display_message: str = False, message: str = None):
        if not self.statusBarObj == None:
            if display_message:
                self.statusBarObj.statusVar.set(message)
            else:
                self.statusBarObj.statusVar.set(self.statusBarObj.default_text)
        
            self.statusBarObj.sbar.update()
    
 
if __name__ == "__main__":
    val = validate()
    returnObj = val.validate_float(12345.76543)
    print(str(returnObj.isValid) + ', ' +  str(returnObj.value))
    
    returnObj = val.validate_decimal(12345.76543, 3)
    print(str(returnObj.isValid) + ', ' +  str(returnObj.value))
    
    returnObj = val.validate_decimal(12345.76543)
    print(str(returnObj.isValid) + ', ' +  str(returnObj.value))
