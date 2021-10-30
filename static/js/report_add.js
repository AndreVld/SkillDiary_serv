$('.report').on('click', function(){   
    id =  $(this).attr('id') 
    add_report = $(this).attr('value') 
    data = {add_report:add_report}
    $.ajax({    
                type:"GET",
                url: 'http://127.0.0.1:8000/course_report/'+id, 
                data: data
                    
            }
            
            
            
            )})