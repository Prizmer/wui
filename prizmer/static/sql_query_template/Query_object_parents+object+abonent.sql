﻿with parent_obj2 as
(with parent_obj as
(SELECT 
  objects.guid as obj_guid, 
  objects.name as obj_name, 
  objects.level,
  objects.guid_parent as parent1_guid
FROM 
  public.objects
)
Select 
  objects.guid as obj_guid2, 
  objects.name as obj_name2, 
  objects.level as level2,
  objects.guid_parent as parent_guid2,
  parent_obj.obj_name
FROM 
  public.objects,
  parent_obj
  where objects.guid_parent=parent_obj.obj_guid
)

Select
  parent_obj2.obj_name,
  parent_obj2.obj_name2,
  objects.name, 
  abonents.name,
  objects.guid,    
  abonents.guid 
 
FROM 
  public.abonents, 
  public.objects,
  parent_obj2
WHERE 
  abonents.guid_objects = objects.guid and 
  objects.guid_parent=parent_obj2.obj_guid2