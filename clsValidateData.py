import tkinter as tk
import clsDates as dateLib
import clsStatusBar as status_bar
import clsStrings as stringLib

# initialise the date class outside the individual classes so it maintains status between calls 
chkDate = dateLib.check_date(None, dateLib.nullDate)
chkDate.allowShortCutKeys = True
            
class dataObj:
    def __init__(self, isValid = False, value = None, widgetJustification = tk.LEFT, toolTip = None):
        self.isValid = isValid
        self.value = value
        self.widgetJustification = widgetJustification
        self.toolTip = toolTip

class validate:
    # This class is used by the GUI to do data type validation and formating.
    # (business logic will need to be elsewhere)
    # Return must always be of type "dataObj"
    
    def __init__(self, statusBarObj = None, errorLogObj = None):
        self.statusBarObj = statusBarObj
        self.errorLogObj = errorLogObj
    
    # ------ Start of Data Type Validations ------
    def validate_decimal(self, value = None, decimal_places = 2):
        formatting = "{: ." + str(decimal_places) + "f}"
        tool_tip = 'Enter a number with ' + str(decimal_places) + ' decimal places.'
        returnObj = dataObj(False, formatting.format(0), tk.RIGHT, tool_tip)
        
        if value:
            try:
                returnObj = dataObj(True, formatting.format(float(value)), returnObj.widgetJustification, tool_tip)
            except Exception as e:
                pass
        
            self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: decimal(' + str(decimal_places) + '))')
        return returnObj
    
    def validate_float(self, value = None):
        tool_tip = 'Enter any number (type: float).'
        returnObj = dataObj(False, 0, tk.RIGHT, tool_tip)
        
        if value:
            try:
                returnObj = dataObj(True, float(value), returnObj.widgetJustification, tool_tip)
            except Exception as e:
                pass
        
            self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: float)')
        return returnObj
    
    def validate_integer(self, value = None):
        tool_tip = 'Enter a whole number (type: integer).'
        returnObj = dataObj(False, 0, tk.RIGHT, tool_tip)
        
        if value:
            try:
                returnObj = dataObj(True, int(value), returnObj.widgetJustification, tool_tip)
                self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: integer)')
            except Exception as e:
                tmpVal = self.validate_float(value)
                if tmpVal.isValid:
                    returnObj = dataObj(True, round(float(value)), returnObj.widgetJustification, tool_tip)
                    if float(value) > float(returnObj.value):
                        self.update_status_bar(True, 'Info: "' + str(value) + '" rounded down (type: integer)')
                    else:
                        self.update_status_bar(True, 'Info: "' + str(value) + '" rounded up (type: integer)')

                else:
                    self.update_status_bar(not returnObj.isValid, 'Error: "' + str(value) + '" not a number (type: integer)')
        return returnObj
    
    def validate_Date(self, value = None):
        returnObj = dataObj(False, dateLib.nullDate, tk.CENTER, dateLib.toolTip)

        if value:
            try:
                chkDate.dateCheck(value)
                self.update_status_bar(not chkDate.isValid, chkDate.messages)                
                returnObj = dataObj(chkDate.isValid, chkDate.formattedDate, returnObj.widgetJustification, dateLib.toolTip)
            except Exception as e:
                pass
        
        return returnObj
    
    def validate_title(self, value = None):
        tool_tip = 'Enter text and it will be formated as a Title.'
        returnObj = dataObj(False, value, tk.LEFT, tool_tip)
        
        if value:
            try:
                strFmt = stringLib.string_format()
                returnObj = dataObj(True, strFmt.title(value), returnObj.widgetJustification, tool_tip)
            except Exception as e:
                pass
        
        return returnObj
    
    def validate_sentence(self, value = None):
        tool_tip = 'Enter text and it will be formated as a Sentence.'
        returnObj = dataObj(False, value, tk.LEFT, tool_tip)
        
        if value:
            try:
                strFmt = stringLib.string_format()
                returnObj = dataObj(True, strFmt.sentence(value), returnObj.widgetJustification, tool_tip)
            except Exception as e:
                pass
        
        return returnObj
    
    # ------ End of Data Type Validations ------
    
    def update_status_bar(self, display_message = False, message = None):
        if not self.statusBarObj == None:
            if display_message:
                self.statusBarObj.statusVar.set(message)
            else:
                self.statusBarObj.statusVar.set(self.statusBarObj.default_text)
        
            self.statusBarObj.sbar.update()
    
 
