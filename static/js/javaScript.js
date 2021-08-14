

// this function to handle checkboxes of table
function hide_show_table(col_name)
{
 var checkbox_val=document.getElementById(col_name).value;
 if(checkbox_val=="hide")
 {
    console.log(col_name+'Hide');
  var all_col=document.getElementsByClassName(col_name);

  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="none";
  }
  console.log(col_name+"_head")

  document.getElementById(col_name+"_head").style.display="none";

  document.getElementById(col_name).value="show";

 }
	
 else
 {
    console.log(col_name+' Show');

  var all_col=document.getElementsByClassName(col_name);
  for(var i=0;i<all_col.length;i++)
  {
   all_col[i].style.display="table-cell";
  }
  document.getElementById(col_name+"_head").style.display="table-cell";
  document.getElementById(col_name).value="hide";
 }
}

// function to handle view button
function EngmodalShow(obj){

    
    // replacing single quote to double so we can convert string to json object
    json_string=obj.replaceAll(`'`, `"`)
    // parse string to convert into JSON object
    json_obj = JSON.parse(json_string);
    // now we can access all key value of object
    document.getElementById("exampleModalLabel").innerHTML = "<strong>"+json_obj.name+" "+json_obj.surname+"</strong>";
    document.getElementById("city").innerHTML = "<p><strong>City:</strong>  "+json_obj.city+"</p>";
    document.getElementById("country").innerHTML = "<p><strong>Country:</strong>  "+json_obj.country+"</p>";
    
    // create a tale row and then append it into table 
    // clear table row first
    document.getElementById('modal-table').getElementsByTagName('tbody')[0].innerHTML=""
    var myHtmlContent = "";
    json_obj.cars.forEach((item) => {
        myHtmlContent+="<tr><td>"+item.id+"</td>"+"<td>"+item.brand+"</td>"+"<td>"+item.model+"</td></tr>"
        var tableRef = document.getElementById('modal-table').getElementsByTagName('tbody')[0];
        var newRow = tableRef.insertRow(tableRef.rows.length);
        newRow.innerHTML = myHtmlContent;
        myHtmlContent = "";
        // document.getElementById("mbody").innerHTML=myHtmlContent
      });

    
}


function ITmodalShow(obj){

    
    // replacing single quote to double so we can convert string to json object
    json_string=obj.replaceAll(`'`, `"`)
    // parse string to convert into JSON object
    json_obj = JSON.parse(json_string);
    // now we can access all key value of object
    document.getElementById("exampleModalLabel").innerHTML = "<strong>"+json_obj.nome+" "+json_obj.cognome+"</strong>";
    document.getElementById("city").innerHTML = "<p><strong>City:</strong>  "+json_obj.citta+"</p>";
    document.getElementById("country").innerHTML = "<p><strong>Country:</strong>  "+json_obj.pease+"</p>";
    
    // create a tale row and then append it into table 
    // clear table row first
    document.getElementById('modal-table').getElementsByTagName('tbody')[0].innerHTML=""
    var myHtmlContent = "";
    json_obj.strada.forEach((item) => {
        myHtmlContent+="<tr><td>"+item.id+"</td>"+"<td>"+item.marca+"</td>"+"<td>"+item.modello+"</td></tr>"
        var tableRef = document.getElementById('modal-table').getElementsByTagName('tbody')[0];
        var newRow = tableRef.insertRow(tableRef.rows.length);
        newRow.innerHTML = myHtmlContent;
        myHtmlContent = "";
        // document.getElementById("mbody").innerHTML=myHtmlContent
      });

    
}