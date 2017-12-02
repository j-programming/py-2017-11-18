#!/usr/bin/env python

class CustomizedException(Exception):
    def __init__(self,message):
        super(CustomizedException,self).__init__(message.upper())



raise CustomizedException('info')