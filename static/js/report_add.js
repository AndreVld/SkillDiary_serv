$('.report').on('click', function(){   
    id =  $(this).attr('id') 
    add_report = $(this).attr('value') 
    data = {add_report:add_report}
    $.ajax({    
                type:"GET",
                url: 'http://www.skilldiary.ru/course_report/'+id, 
                data: data
                    
            }
            
            )})