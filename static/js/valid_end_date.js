$(document).ready(function () {
   
    $('#id_end_date').on('change', function(){  
        form = document.getElementsByClassName("form-task");
        id =  $(form).attr('id') 
        $.ajax({
            data: $(this).serialize(), 
            url:  'http://www.skilldiary.ru/course/'+ id +'/validate_enddate/',
            success: function (response) {
                if (response.is_taken == 'True' ) {
                    $('.errorlist').remove();
                    $('.invalid-enddate').remove();
                    $('.date-wrap').after('<div class="invalid-enddate"> Дата окончания выходит за период курса!</div>')
                    $('#button').attr('disabled', true);
                }
                else {
                    $('.errorlist').remove();
                    $('.invalid-enddate').remove();
                    if ($('.invalid-startdate').length == 0) { 
                        $('#button').attr('disabled', false);
                       
                    }
                    else {
                        
                        $('#button').attr('disabled', true);
                    }                    
                }
            },
         
            error: function (response) {
                console.log('error')
            }
        });
        return false;
    });
})