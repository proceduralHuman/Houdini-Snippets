wallIdNamesList = ["apple", "banana", "cherry"]

def createWallNode(kwargs):
    node = hou.pwd()
    #print "thisNode"+str(node.path())
    parm_group = node.parmTemplateGroup()
    target_folder = parm_group.findFolder(("Setup Walls",))
    
    thisWallNode = hou.node('../'+str(node)+'/walls2').createNode("w_bir_walldetails")
    
    inputNode = hou.node('../'+str(node)+'/walls2/InputForWallNodes') 
    outputNode_1 = hou.node('../'+str(node)+'/walls2/Merge_WallElements')
    outputNode_2 = hou.node('../'+str(node)+'/walls2/Merge_addElementsWallElements')

    
    thisWallNode.setInput(0, inputNode)
    outputNode_1.setNextInput(thisWallNode, 0)
    outputNode_2.setNextInput(thisWallNode, 1)   
    
    wallIDLabel = node.parm("idName").eval()

    nameAlreadyExists = False
    for i in range(0,len(wallIdNamesList)):
        if(str(wallIdNamesList[i]) == str(wallIDLabel)):
            nameAlreadyExists = True
    
    if len(wallIDLabel) <= 1 or nameAlreadyExists == True:
        wallIDLabel ="wallNode" + str(node.parm("IDCount").eval())
    #wallIdNames.append(str(wallIDLabel))
    parm_folder = hou.FolderParmTemplate("wallNode" + str(node.parm("IDCount").eval()),
                                         wallIDLabel,
                                         folder_type=hou.folderType.RadioButtons)
                                 
    parm_folder.addParmTemplate(hou.IntParmTemplate("wallID" + str(node.parm("IDCount").eval()), "Wall ID", 1))
    expression = 'chs("'+str(node.path())+'/wallID'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("wallID").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("i_wallDetail"+ str(node.parm("IDCount").eval()), "Input Wall Detail"+ str(node.parm("IDCount").eval()), 1, naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chsop("../../'+'i_wallDetail'+ str(node.parm("IDCount").eval())+'")' 
    thisWallNode.parm("i_WallDetailsGeo").setExpression(expression) 
        
    parm_folder.addParmTemplate(hou.StringParmTemplate("i_wallCutGeo"+ str(node.parm("IDCount").eval()), "Input Wall Cut Geo"+ str(node.parm("IDCount").eval()), 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" == 3 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chsop("../../'+'i_wallCutGeo'+ str(node.parm("IDCount").eval())+'")' 
    #expression = 'if(opexist(chs("'+str(node.path())+'/i_wallCutGeo'+ str(node.parm("IDCount").eval())+'")),'+'chs("'+str(node.path())+'/i_wallCutGeo'+ str(node.parm("IDCount").eval())+',"../Placeholder")'
    thisWallNode.parm("i_WallCutOutGeo").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("i_alternativeGeo"+ str(node.parm("IDCount").eval()), "Input Alternative Geo"+ str(node.parm("IDCount").eval()), 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 3 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chsop("../../'+'i_alternativeGeo'+ str(node.parm("IDCount").eval())+'")' 
    #expression = 'if(opexist(chs("'+str(node.path())+'/i_alternativeGeo'+ str(node.parm("IDCount").eval())+'")),'+'chs("'+str(node.path())+'/i_alternativeGeo'+ str(node.parm("IDCount").eval())+',"../Placeholder")'
    thisWallNode.parm("i_AltGeo").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("widthInputSeg" + str(node.parm("IDCount").eval()), "Width of Input Segment", 1, default_value = (8,0,0),  disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" == 3 }"))
    expression = 'chs("'+str(node.path())+'/widthInputSeg'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("widthOfPart").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.ToggleParmTemplate("useHeightAdjustment" + str(node.parm("IDCount").eval()), "Use height adjustment", default_value = True,disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 3 }", default_expression_language=hou.scriptLanguage.Python))
    expression = 'ch("'+str(node.path())+'/useHeightAdjustment'+ str(node.parm("IDCount").eval())+'")'    
    thisWallNode.parm("heightAdjustmentToggle").setExpression(expression) 
    
    
    
    parm_folder.addParmTemplate(hou.IntParmTemplate("mode"+ str(node.parm("IDCount").eval()), "Switch Mode", 1, menu_items=(["0","1","2","3","4"]), menu_labels=(["Centered","Align on one edge","Align on two edges","borderless","randomPlacement"]), item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/mode'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("mode").setExpression(expression) 
    
   
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("minWidth" + str(node.parm("IDCount").eval()), "Min width for main input", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 3 }"))
    expression = 'chs("'+str(node.path())+'/minWidth'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("minWidth").setExpression(expression) 
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("offsetWidth" + str(node.parm("IDCount").eval()), "Offset width", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 3 }"))
    expression = 'chs("'+str(node.path())+'/offsetWidth'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("offsetWidth").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("relPointsNormals" + str(node.parm("IDCount").eval()), "Relevant snapping points by x normals", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 3 }"))
    expression = 'chs("'+str(node.path())+'/relPointsNormals'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("ptSnappingNormalsThres").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.IntParmTemplate("invAlignment" + str(node.parm("IDCount").eval()), "invert alignment", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 2 }"))
    expression = 'chs("'+str(node.path())+'/invAlignment'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("invertAlignment").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("offset" + str(node.parm("IDCount").eval()), "Offset", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 2 }"))
    expression = 'chs("'+str(node.path())+'/offset'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("offset").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("offsetSingleFromEdge" + str(node.parm("IDCount").eval()), "Offset", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 1 }"))
    expression = 'chs("'+str(node.path())+'/offsetSingleFromEdge'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("offsetSingleFromEdge").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("randObj_1_"+ str(node.parm("IDCount").eval()), "Input RandObj 1", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/randObj_1_'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("randObj_1").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("randObjCutout_1_"+ str(node.parm("IDCount").eval()), "Input RandObj 1 Cutout", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/randObjCutout_1_'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("randCutout_1").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.SeparatorParmTemplate ("seperator_1"+ str(node.parm("IDCount").eval())))
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("randObj_2_"+ str(node.parm("IDCount").eval()), "Input RandObj 2", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/randObj_2_'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("randObj_2").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("randObjCutout_2_"+ str(node.parm("IDCount").eval()), "Input RandObj 2 Cutout", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/randObjCutout_2_'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("randCutout_2").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.SeparatorParmTemplate ("seperator_2"+ str(node.parm("IDCount").eval())))

    
    parm_folder.addParmTemplate(hou.StringParmTemplate("randObj_3_"+ str(node.parm("IDCount").eval()), "Input RandObj 3", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/randObj_3_'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("randObj_3").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.StringParmTemplate("randObjCutout_3_"+ str(node.parm("IDCount").eval()), "Input RandObj 3 Cutout", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }", default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal))
    expression = 'chs("'+str(node.path())+'/randObjCutout_3_'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("randCutout_3").setExpression(expression) 
    
    
    parm_folder.addParmTemplate(hou.SeparatorParmTemplate ("seperator_3"+ str(node.parm("IDCount").eval())))

    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("borderDepth" + str(node.parm("IDCount").eval()), "BorderDepth", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }"))
    expression = 'chs("'+str(node.path())+'/borderDepth'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("borderDepth").setExpression(expression) 
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("sizeOfArea" + str(node.parm("IDCount").eval()), "Size of Area", 3, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }"))   
    expressionX = 'chs("'+str(node.path())+'/sizeOfArea'+ str(node.parm("IDCount").eval())+'x")'
    expressionY = 'chs("'+str(node.path())+'/sizeOfArea'+ str(node.parm("IDCount").eval())+'y")'
    expressionZ = 'chs("'+str(node.path())+'/sizeOfArea'+ str(node.parm("IDCount").eval())+'z")'
    thisWallNode.parm("sizex").setExpression(expressionX) 
    thisWallNode.parm("sizey").setExpression(expressionY) 
    thisWallNode.parm("sizez").setExpression(expressionZ) 
    
    
    parm_folder.addParmTemplate(hou.FloatParmTemplate("snapDistance" + str(node.parm("IDCount").eval()), "SnapDistance", 1, disable_when ="{ mode"+ str(node.parm("IDCount").eval())+" != 4 }"))
    expression = 'chs("'+str(node.path())+'/snapDistance'+ str(node.parm("IDCount").eval())+'")'
    thisWallNode.parm("tol3d").setExpression(expression) 
    
    
    
    
    
    thisNodeName = hou.StringParmTemplate("nodeName"+ str(node.parm("IDCount").eval()), "Link", 1, (str(thisWallNode),), hou.parmNamingScheme.Base1)# 
    parm_folder.addParmTemplate(thisNodeName)
    
    removeBtn = hou.ButtonParmTemplate("buttonName"+str(node.parm("IDCount").eval()), "Remove")
    removeBtn.setScriptCallback("hou.phm().removeWallID('"+str(thisWallNode)+"', '"+str(parm_group)+"','"+str(parm_folder.name())+"', kwargs)")
    removeBtn.setScriptCallbackLanguage(hou.scriptLanguage.Python)
    parm_folder.addParmTemplate(removeBtn)
        
    
    parm_group.appendToFolder(target_folder, parm_folder)
    node.setParmTemplateGroup(parm_group)

    #increase ID count
    newVal = node.parm("IDCount").eval() + 1
    node.parm("IDCount").set(newVal)



    
def removeWallID(insideNode, parmGroupName, folderName, kwargs):
    node = hou.pwd()
    thisInsideNode = hou.node('../'+str(node)+'/walls2/'+str(insideNode))   
    if thisInsideNode is not None:
        #disconnect outputs:
        outs = thisInsideNode.outputConnections()
        for outCon in outs:
            outIndex = outCon.inputIndex()
            outNode = outCon.outputNode()
            outNode.setInput(outIndex,None,0)
            
        thisInsideNode.destroy()
    null_tg = node.parmTemplateGroup()
    null_tg.remove(folderName) 
    #setting the template
    node.setParmTemplateGroup(null_tg)


    
    