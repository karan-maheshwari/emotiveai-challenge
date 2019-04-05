$(document).ready(function(e){
    $("#save").click(function(e){
    e.preventDefault();
    var form1Data = $('#keyword_form').serialize();
    $.ajax({
        url : '/process',
        type : 'post',
        datatype : 'json',
        data : form1Data
    });
  });
});

$(document).ready(function(e){
    $("#send_individual").click(function(e){
    e.preventDefault();
    var form1Data = $('#individual_message').serialize();
    $.ajax({
        url : '/send_individual',
        type : 'post',
        datatype : 'json',
        data : form1Data
    });
  });
});

$(document).ready(function(e){
    $("#send_blast").click(function(e){
    e.preventDefault();
    var form1Data = $('#blast_message').serialize();
    $.ajax({
        url : '/send_blast',
        type : 'post',
        datatype : 'json',
        data : form1Data
    });
  });
});
