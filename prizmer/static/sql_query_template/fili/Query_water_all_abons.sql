With obj as 
(Select guid as guid_child, objects.name as name_child, objects.level as level_child, guid_parent as guid_parent_child
 from objects)
Select guid as grand_parent, objects.name as name_parent, objects.level, objects.guid_parent, 
obj.guid_child,obj.name_child, obj.level_child, obj.guid_parent_child
FROM 
  public.objects, obj
where obj.guid_parent_child=objects.guid
and objects.name='Мичуринский 26 к.А' 
and obj.name_child='Квартира 504'
order by name_parent
