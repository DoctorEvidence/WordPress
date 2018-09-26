<?php  
/**
*  @package PaoloPlugin
   Plugin Name: DRE Plugin
   Description: Plugin to fetch stats from DOC Search
   Version: 1.0.0
   Author: Paolo Bondi
*/
function box() {

#Fetches JSON and returns it
function login(){
  ob_start();
$curl = curl_init();

#Sends a GET to the API using OAuth tokens
curl_setopt_array($curl, array(
  CURLOPT_URL => "https://search.doctorevidence.com/api/trends/stats",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "GET",
  CURLOPT_HTTPHEADER => array(
    "authorization: Bearer LDW3Nhkdmc7ulnAbigJJQAAzlI4_EDDw",
    "cache-control: no-cache"
  ),
));

$response = curl_exec($curl);
$err = curl_error($curl);
$obj = json_decode($response, true);
curl_close($curl);

if ($err) {
  echo "cURL Error #:" . $err;
} else {
  return $obj;

}

}
#Assigns JSON to $done 
$done = login();

#Bolded text/values
$label_count = number_format((round(floatval($done["label-count"]), -5, PHP_ROUND_HALF_UP))/1000000,1);
$term_count = number_format(round(floatval($done["term-count"]), -5, PHP_ROUND_HALF_UP)/1000000,1);
$article_count = number_format(round(floatval($done["article-count"]), -6, PHP_ROUND_HALF_UP)/1000000, 1);

#Lighter text/values
$clinical_trials =number_format($done["clinicaltrials-count"]);
$epar = number_format($done["epar-count"]);
$feed_entries_count = number_format($done["feed-entries-count"]);
$asco = number_format($done["asco-count"]);
$feed_count = floatval($done["feed-count"]);
$pub_med = number_format(round(floatval($done["medline-count"]))/1000000, 1);
$news = number_format(floatval($done["articles-by-category"]["news"]));
$official = number_format(floatval($done["articles-by-category"]["official"]));
$social = number_format(floatval($done["articles-by-category"]["social"]));

?>
<style>
object {
   background-color: #EDEDED; 
   display: block; 
   width: 1350px;
   height: auto;
   padding: 15px;
   border-radius: 7px; 
   margin-right: auto;
   margin-left: auto;
   text-align: center;
   
   }
   h2 {
   font-weight: bolder;
   font-size: 20;
   }

   h3{
      font-weight: lighter;
   }
</style>


<!DOCTYPE html>
<html>
<body>
   <object> 
      <h2>
         <font color="#545454";> 
            Our database currently contains ~<?php echo $article_count; ?> million documents and <?php echo $term_count; ?> million concepts (<?php echo $label_count; ?> million terms).
         </font> 
      </h2>
   <h3>
      <font color ="#555555">
         We currently index <a href="https://www.ncbi.nlm.nih.gov/pubmed/"> PubMed</a> (<?php echo $pub_med . " million"; ?>),  <a href="http://www.clinicaltrials.gov"> ClinicalTrials.gov</a>  (<?php echo $clinical_trials; ?>), EPAR (<?php echo $epar; ?>), ASCO (<?php echo $asco;?>), RSS feeds (<?php echo $feed_entries_count; echo " from " . $feed_count . " feeds"?>).
      </font>
   </h3>
   <h3>
      <font color="#555555">
         Number of items per feed category: news: <?php echo $news; ?>, official: <?php echo $official; ?>, social: <?php echo $social ?>
      </font>
   </h3>
   </object>
</body>
</html>

<?php
  return ob_get_clean();
  }
 add_shortcode('box', 'box');
 ?>
