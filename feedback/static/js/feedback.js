$(':radio').change(
  function(){
    $('.choice').text( $(this).val() + ' stars' );
  }
)
