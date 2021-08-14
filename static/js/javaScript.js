

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
