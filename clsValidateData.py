import tkinter as tk
import clsDates as dateLib
import clsStatusBar as status_bar

chkDate = dateLib.check_date(None, dateLib.nullDate)
chkDate.allowShortCutKeys = True

class validate:
    def __init__(self, statusBarObj = None, errorLogObj = None):
        self.statusBarObj = statusBarObj
        self.errorLogObj = errorLogObj
    
    # ------ Start of Data Type Validations ------
    def validate_decimal(self, value = None, decimal_places = 2):
        formatting = "{: ." + str(decimal_places) + "f}"
        tool_tip = 'Enter a number with ' + str(decimal_places) + ' places.'
        returnObj = dataObj(False, formatting.format(0), tk.RIGHT, tool_tip)
        
        if value:
            try:
                returnObj = dataObj(True, formatting.format(float(value)), returnObj.widgetJustification, tool_tip)
            except Exception as e:
                pass
        
            self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: decimal(' + str(decimal_places) + '))')
        return (returnObj.isValid,returnObj.value,returnObj.widgetJustification,returnObj.toolTip)
    
    def validate_float(self, value = None):
        returnValue = (False, 0, tk.RIGHT, None)
        
        if value:
            try:
                returnValue = (True, float(value), returnValue[2], None)
            except Exception as e:
                pass
        
            self.update_status_bar(not returnValue[0], 'Error: "' + str(value) + '" not a number (type: float)')
        return returnValue
    
    def validate_integer(self, value = None):
        returnValue = (False, 0, tk.RIGHT, None)
        
        if value:
            try:
                returnValue = (True, int(value), returnValue[2], None)
                self.update_status_bar(not returnValue[0], 'Error: "' + str(value) + '" not a number (type: integer)')
            except Exception as e:
                tmpVal = self.validate_float(value)
                if tmpVal[0]:
                    returnValue = (True, round(float(value)), returnValue[2], None)
                    if float(value) > float(returnValue[1]):
                        self.update_status_bar(True, 'Info: "' + str(value) + '" rounded down (type: integer)')
                    else:
                        self.update_status_bar(True, 'Info: "' + str(value) + '" rounded up (type: integer)')
                else:
                    self.update_status_bar(not returnValue[0], 'Error: "' + str(value) + '" not a number (type: integer)')
        return returnValue
    
    def validate_Date(self, value = None):
        returnValue = (False, dateLib.nullDate, tk.CENTER, 'Date Stuff')
        print(value)
        if value:
            try:
                chkDate.dateCheck(value)
                self.update_status_bar(not chkDate.isValid, chkDate.messages)                
                returnValue = (chkDate.isValid, chkDate.formattedDate, returnValue[2], 'Date Stuff')
            except Exception as e:
                pass
        
        return returnValue
    # ------ End of Data Type Validations ------
    
    def update_status_bar(self, display_message = False, message = None):
        if not self.statusBarObj == None:
            if display_message:
                self.statusBarObj.statusVar.set(message)
            else:
                self.statusBarObj.statusVar.set(self.statusBarObj.default_text)
        
            self.statusBarObj.sbar.update()
            
class dataObj:
    def __init__(self, isValid = False, value = None, widgetJustification = tk.LEFT, toolTip = None):
        self.isValid = isValid
        self.value = value
        self.widgetJustification = widgetJustification
        self.toolTip = toolTip
    
    