<?php
require_once("classes/MemberClass.php");
include("mysql/membersite_config.php");
//include("mysql/checkuser.php");
include("includes/bootstrap_header.html");
error_reporting(E_ERROR);

	$id = stripslashes($_GET['id']);

	if($id !=""){
		 	$url = $fgmembersite->curPageURL();
		 	$totCollected = 0;
		 	
			include("mysql/select-event.php");
			
			$typeEvent = $EventType;
			
			//connect include
			require("mysql/connect-mysqli.php");
			require_once("classes/MemberClass.php");

			include("mysql/isAd.php");

			$random = $fgmembersite->GetSiteNum();

			$EventDate = "";

			if($StartDate == $EndDate)
				$EventDate = date("M d, Y", strtotime($StartDate));
			else
				$EventDate =date("M d, Y", strtotime($StartDate)) . " - " . date("M d, Y", strtotime($EndDate));


			$EventName = $fgmembersite->removeBackslash($EventName);
			$EventNameOrig = $EventName;
			$eName = $EventName;
			$canAdd = false;

			if($isAdmin)
			{
	 			$EventName = "<a class='title' href='https://www.usictennis.org/manage/edit-event.html?id=".$id."'>" . $EventName . "</a>";
			}

			if(isset($_SESSION['mid']) && !empty($_SESSION['mid'])) {

					$mid = $_SESSION['mid'];
					
					$canAdd = false;

					$eventid = $id;

					include("mysql/isCaptain.php");

					if($isAdmin)
						$canAdd = true;

					$canSeeMatchFee = false;

					$isInterestedMember = false;

					$sql ="SELECT MemberId FROM matchinterestedmember WHERE MatchId = ? AND MemberId = ?";

					$stmt = $link->prepare($sql);

					$stmt->bind_param("ss", $eventid, $mid);

					$stmt->execute();

					$stmt->store_result();;

					$InterestedMemberCnt = $stmt->num_rows;

					if($InterestedMemberCnt > 0)
						$isInterestedMember = true;

					$stmt->close();

					$isConfirmedMember = false;

					$sql ="SELECT MemberId FROM membermatch WHERE MatchId = ? AND MemberId = ?";

					$stmt = $link->prepare($sql);

					$stmt->bind_param("ss", $eventid, $mid);

					$stmt->execute();

					$stmt->store_result();;

					$ConfirmedMemberCnt = $stmt->num_rows;

					if($ConfirmedMemberCnt > 0)
						$isConfirmedMember = true;

					$stmt->close();
				}
				
			
				
				//end fee access setup
              
				echo "
				<div class='container container-padding'>";

				
					echo "<div class='col-md-6 pull-right'>";
					
					//get fees
					$sql ="SELECT ID, MatchId, Price FROM fees WHERE fees.MatchId = ? AND Type = 'MATCH' AND (IsViewable is NULL OR IsViewable = 1)";
					
					$stmt = $link->prepare($sql);
					
					$stmt->bind_param("s", $id);
					
					$stmt->execute();
					
					$stmt->bind_result($feeId, $matchId, $price);
					
					$stmt->store_result();;
					
					$feenumrows = $stmt->num_rows;
						
					
					$feesFound =false;

					$feeSelection = "<select id='selectFee' class='pull-right'>";
					$feeDisplay = "";
					if($feenumrows == 1)
					{
						$feesFound = true;
						while ($stmt->fetch()) {
							//echo "<a class='pull-right' href='/member/fee/" .$feeId. "'>Pay Member Match Fee</a>";
							//echo "<input type='button' id='btnMatchFee' class='btn btn-xs  btn-border btnPayFee'  data-value='" .$feeId. "' value='Pay Match Fee' />";
							$feeSelection .= "<option value='" .$feeId. "' >Match Fee $". $price ."</option>";
							$feeDisplay .= "<p>Match Fee: $". $price ."</p>";
						}
					}

					$stmt->close();

					$sql ="SELECT ID, MatchId, Description, Price FROM fees WHERE fees.MatchId = ? AND Type = 'OTHER' AND (IsViewable is NULL OR IsViewable = 1) ORDER BY DateInserted DESC";

					$stmt = $link->prepare($sql);

					$stmt->bind_param("s", $id);

					$stmt->execute();

					$stmt->bind_result($feeId, $matchId, $desc, $price);

					$stmt->store_result();

					$feenumrows = $stmt->num_rows;

					if($feenumrows > 0)
					{
						$feesFound = true;
						while ($stmt->fetch()) {
							//echo "<br/><a class='pull-right' href='/member/fee/" .$feeId. "'>Pay '". $desc . "'</a>";
							//echo "&nbsp;<input type='button' id='btnOtherFee' class='btn btn-xs  btn-border  btnPayFee'  data-value='" .$feeId. "' value='Pay ". $desc . "' />";
							$feeSelection .= "<option value='" .$feeId. "' >" . $desc . " $". $price ."</option>";
							$feeDisplay .= "<p>". $desc . ": $". $price ."</p>";
						}
					}

					$stmt->close();

					if($feesFound){
						
						//must be confirmed or interested member to pay fee
						if( ($isAdmin || $isCaptain || $isConfirmedMember || $isInterestedMember))
						{
							echo "<span class='pull-right' style='padding-left:5px;'><input type='button' id='btnPayFee' class='btn btn-xs  btn-border btnPayFee pull-right'  value='Add to Cart' /></span>";
							echo $feeSelection;
							echo "</select>&nbsp;&nbsp;";
						}					
					}

				echo "</div>";

			echo "<table id=\"eventpage\" summary=\"Event Detail\">
				<tr>
					<th class=\"title\" style=\"text-decoration:none\" colspan=\"3\">" . $EventName . "</th>
				</tr>
				<tr>
					<td style=\"vertical-align:top\" class=\"eventpageimg\"><img  class='img-responsive' src=\"../" . $PhotoLink . "\" /></td>
					<td style=\"vertical-align:top\"></td>
				</tr>
				<tr>
					<td style=\"vertical-align:top;text-align:left\" colspan=2>
						<table >
							<tr>
								<td class=\"eventpagedetail-first\" >Date:&nbsp;</td>
								<td>" . $EventDate . "</td>
							</tr>
							<tr>
								<td class=\"eventpagedetail-first\">Location:&nbsp;</td>
								<td>" . $City . ", " . $Country . "</td>
							</tr>";
							if ($VenueName != NULL)
							{
							echo "
							<tr>
								<td class=\"eventpagedetail-first\">Venue:&nbsp;</td>
								<td>" . $VenueName . "</td>
							</tr>";
							}
							if ($GalleryLink != NULL)
							{
								echo "
							<tr>
								<td class=\"eventpagedetail-first\">Photos:&nbsp;</td>
								<td style='text-align:left'><a target='_blank' href=\"../gallery.php?id=" . $id . "\">USIC photo gallery</a></td>
							</tr>";
							}
							echo "
						</table>
					</td>

				</tr>
				</table>
			";

	echo "<div class='row'>";
	if (($WomensCaptain != NULL) || ($MensCaptain != NULL))
	{
			echo "
					<div class=\"divider\"></div>
					<div class='row' style='padding-left:15px'>
						<div class='col-md-6'>
							<span class='title'><b>USIC Captain Information</b></span>
						</div>

					</div> <!--end row-->
			";
			if($MensCaptain != NULL){
				echo " <div class='col-md-5'>
						<table id='bootstraptable'>
							<tr>
								<td class=\"eventpagedetail-first\" >";
								if($WomensCaptain == NULL)
								echo "Captain:";
								else
								echo "Men's Captain:";
								echo "</td>";

								if($MenCaptainLink != NULL && (isset($_SESSION['mid']) && !empty($_SESSION['mid'])) )
								{

									echo "<td> <a href='https://www.usictennis.org/member-info/" . $MenCaptainLink . "'>". $MensCaptain ."</a></td>";
								}
								else
								{
									echo "<td>" . $MensCaptain . "</td>";
								}
							echo "</tr>";

		            echo "</table>
		               </div> <!-- end col-md-5 -->";
			}

			if($WomensCaptain != NULL){
				echo "<div class='col-md-5'>
						<table id='bootstraptable'>
							<tr>
								<td class=\"eventpagedetail-first\" >";

								if($MensCaptain == NULL)
									echo "Captain:";
								else
									echo "Women's Captain:";
								echo "</td>";
								if($WomenCaptainLink != NULL && (isset($_SESSION['mid']) && !empty($_SESSION['mid'])))
								{
									echo "<td> <a href='https://www.usictennis.org/member-info/" . $WomenCaptainLink . "'>". $WomensCaptain ."</a></td>";
								}
								else
								{
									echo "<td>" . $WomensCaptain . "</td>";
								}
							echo "</tr>";
				echo	"</table>
					  </div> <!-- end col-md-5 -->";
			}

			echo "</div> <!--end row--> ";


		echo "	<div class='row' style='padding-top:8px'>";

		if (($WomensCaptain2 != NULL) || ($MensCaptain2 != NULL))
		{
			if ($MensCaptain2 != NULL)
			{
				echo "	<div class='col-md-5'>
							<table id='bootstraptable'>
								<tr>
									<td class=\"eventpagedetail-first\" >Co-Captain:</td>";
									if($MenCaptainLink2 != NULL && (isset($_SESSION['mid']) && !empty($_SESSION['mid'])))
									{
										echo "<td> <a href='https://www.usictennis.org/member-info/" . $MenCaptainLink2 . "'>". $MensCaptain2 ."</a></td>";
									}
									else
									{
										echo "<td>" . $MensCaptain2 . "</td>";
									}

				echo "	 	   </tr>";

				echo "	    </table>
						</div>";
			}

			if ($WomensCaptain2 != NULL)
			{
				echo "<div class='col-md-5'>
						<table id='bootstraptable'>
								<tr>
									<td class=\"eventpagedetail-first\" >Co-Captain:</td>";
									if($WomenCaptainLink2 != NULL && (isset($_SESSION['mid']) && !empty($_SESSION['mid'])))
										{
											echo "<td> <a href='https://www.usictennis.org/member-info/" . $WomenCaptainLink2 . "'>". $WomensCaptain2 ."</a></td>";
										}
										else
										{
											echo "<td>" . $WomensCaptain2 . "</td>";
										}
							echo "</tr>";
					echo "	</table>
					   </div> <!--col-md-5-->";
			}
		}
	}
		echo "</div> <!--row-->";

		if ($Recap != NULL)
		{
			echo "

				<table id=\"eventpage\" summary=\"Recap\" class=\"col-md-12 voffset2\">
				<tr>
					<th class='title'>Recap</th>
				</tr>
				</table>
			";
			echo "<div class='col-md-12'>";
			echo stripslashes($fgmembersite->replaceReturnWithBR($Recap));
			echo "</div>";
		}
		
				
		if ($Results != NULL)
		{
			echo "
			<div class=\"divider\"></div>
				<table id=\"eventpage\" summary=\"Results\">
				<tr>
						<th class=\"title\">Results</th>
				</tr>
				<tr>
					<td>" . stripslashes($fgmembersite->replaceReturnWithBR($Results)) ."</td>
				</tr>
				<tr>
					<td>&nbsp;</td>
				</tr>
			</table>
			";
		}
		
		

		$playerextract = "Select distinct ml.MemberID, FirstName, LastName, MiddleName, NickName, DOB,
				Type, mm.MatchID, NonMemberName, IFNULL(IsSpouse,0), IFNULL(IsAlternate,0), 0 as IsApproved
				from memberlist ml, membermatch mm where mm.gender='M' 
				and ml.MemberID = mm.MemberID 
				and mm.MatchID = ? 
				and (mm.NonPlaying = 0 or  mm.NonPlaying is null) 
				order by LastName, FirstName";

		$stmt = $link->prepare($playerextract);

		$stmt->bind_param("s", $EventID);

 		$stmt->execute();

 		$stmt->store_result();

		$playersnumrows = $stmt->num_rows;

		$stmt->close();

		$playerextractWomen = "Select distinct ml.MemberID, FirstName, LastName, MiddleName, NickName, DOB, 
				Type, mm.MatchID, NonMemberName, IFNULL(IsSpouse,0), IFNULL(IsAlternate,0), 0 as IsApproved  
				from memberlist ml, membermatch mm 
				where mm.gender = 'F' 
				and ml.MemberID = mm.MemberID 
				and mm.MatchID = ? 
				and (mm.NonPlaying = 0 or  mm.NonPlaying is null)	
				order by LastName, FirstName";

		$stmt = $link->prepare($playerextractWomen);

		$stmt->bind_param("s", $EventID);

 		$stmt->execute();

 		$stmt->store_result();

		$playersnumrowsWomen = $stmt->num_rows;

		$stmt->close();
		
		//non-playing men and women members
		$npExtract = "Select distinct ml.MemberID, FirstName, LastName, MiddleName, NickName, DOB, 
				Type, mm.MatchID , IFNULL(mm.NonMemberName, ''), IFNULL(mm.IsSpouse,0), IFNULL(mm.IsAlternate,0), 0 as IsApproved
				from memberlist ml, membermatch mm 
				where ml.MemberID = mm.MemberID 
				and mm.MatchID = ? and mm.NonPlaying = 1 
				and (mm.IsSpouse is null or mm.IsSpouse = 0) 
				order by LastName";
		
		$stmt = $link->prepare($npExtract);
		
		$stmt->bind_param("s", $EventID);
		
		$stmt->execute();
		
		$stmt->store_result();
		
		$npNumrows = $stmt->num_rows;
		
		$stmt->close();
		
		//men spouse non-playing
		$nonPlayMenSpouse = "Select distinct ml.MemberID, FirstName, LastName, MiddleName, NickName, DOB, 
				Type, mm.MatchID, IFNULL(mm.NonMemberName, ''), IFNULL(mm.IsSpouse,0) , IFNULL(mm.IsAlternate,0), 0 as IsApproved
				from memberlist ml, membermatch mm 
				where mm.gender='M' 
				and ml.MemberID = mm.MemberID 
				and mm.MatchID = ? 
				and mm.NonPlaying = 1 
				and mm.IsSpouse = 1
				order by LastName";
		
		$stmt = $link->prepare($nonPlayMenSpouse);
		
		$stmt->bind_param("s", $EventID);
		
		$stmt->execute();
		
		$stmt->store_result();
		
		$nonPlayMenSpouseRows = $stmt->num_rows;
		
		$stmt->close();
		
		//women spouse non-playing
		$nonPlayWomenSpouse = "Select distinct ml.MemberID, FirstName, LastName, MiddleName, NickName, DOB, 
				Type, mm.MatchID, IFNULL(mm.NonMemberName, ''), IFNULL(mm.IsSpouse,0), IFNULL(mm.IsAlternate,0), 0 as IsApproved
				from memberlist ml, membermatch mm 
				where mm.gender='F' 
				and ml.MemberID = mm.MemberID 
				and mm.MatchID = ? 
				and mm.NonPlaying = 1 
				and mm.IsSpouse = 1 
				order by LastName";
		
		$stmt = $link->prepare($nonPlayWomenSpouse);
		
		$stmt->bind_param("s", $EventID);
		
		$stmt->execute();
		
		$stmt->store_result();
		
		$nonPlayWomenSpouseRows = $stmt->num_rows;
		
		$stmt->close();
		

		
// 		if(!empty($_SESSION['mid']) && $feesFound )
// 		{
		
// 			echo "
// 			<div class=\"divider\"></div>
// 				<table id=\"eventpage\" summary=\"Results\">
// 				<tr>
// 						<th class=\"title\">Event Fees</th>
// 				</tr>
// 				<tr>
// 					<td>" . $feeDisplay ."</td>
// 				</tr>
// 				<tr>
// 					<td>&nbsp;</td>
// 				</tr>
// 			</table>
// 			";
		
// 		}
		
		
		if($playersnumrows > 0 || $playersnumrowsWomen > 0){

			$playersTitle = "Players";

			echo "
				<div class=\"divider\"></div>";

				if($isCaptain || $isAdmin){
					echo "<div class='pull-left col-md-12'><a href='javascript:;' class='pull-right' id='print'>Printable Summary</a></div>";
				}
			echo  "<table id=\"tblConfirmed\" summary=\"Players\">
					<tr>
						<th class=\"title\">$playersTitle</th>
					</tr>";

			if($playersnumrowsWomen > 0){

				echo "<tr><td><b>Women</b></td></tr>";
				$totCollected +=$fgmembersite->outputPlayerInfo($playerextractWomen, $EventID, $StartDate, $link, $url, $fgmembersite, false, $canAdd, false, $typeEvent);
				
				echo "<tr><td>&nbsp;</td></tr>";
			}

			if($playersnumrows > 0){

				echo "<tr><td><b>Men</b></td></tr>";
				$totCollected +=$fgmembersite->outputPlayerInfo($playerextract, $EventID, $StartDate, $link, $url, $fgmembersite, false, $canAdd, false, $typeEvent);
			}

			if ($PlayersWomen != NULL ||$PlayersWomen != "" || $Players != NULL || $Players != "" ){
				echo "<tr><td colspan='2'>&nbsp;</td></tr>";
				echo "<tr><td colspan='2'><b><i>Guests/Proposed Members</i></b></td></tr>";
				echo "<tr><td colspan='2'>&nbsp;</td></tr>";

				if ($PlayersWomen != NULL){

					echo "<tr><td><b>Women</b></td></tr>";
					echo "<tr><td>" . $PlayersWomen ."</td></tr>";
					echo "<tr><td>&nbsp;</td></tr>";
				}

				if ($Players != NULL){

					echo "<tr><td><b>Men</b></td></tr>";
					echo "<tr><td>" . $Players ."</td></tr>";
				}
			}
			if($canAdd){

			$donationExtract = "select ml.FirstName, ml.LastName, ml.MiddleName, t.MemberId, DonationAmount, Description, ShortDescription
						from transaction t
						inner join memberlist ml on  t.MemberId = ml.MemberId
						where description like 'Donation " . $fgmembersite->SanitizeForSQL($link,$EventNameOrig) ."%'".
						" and ShortDescription = 'DONATE'";

			$stmt = $link->prepare($donationExtract);

			$stmt->execute();

			$stmt->bind_result($donFName, $donLName, $donMName, $donMid, $donAmt, $donDesc, $donSD);

			$stmt->store_result();

			$stmt->fetch();

			$donationsCount = $stmt->num_rows;

			$stmt->close();

			//donations
			if($donationsCount > 0)
			{
				echo "<tr><td colspan=2>&nbsp;</td>";
				echo "<tr><td colspan=2><b>Donations</b></td>";
				echo "<tr><td class='". $donMid  ."'>" . $donFName. " " . $donLName . "</td>".
				"<td class='feeAmountColl'>$" . $donAmt . "</td>" ."</tr>";
				echo "<tr><td colspan=2>&nbsp;</td>";
			}

				
			}
			echo "</table>";
		}
		else if ($Players != NULL)
		{

			echo "<div class=\"divider\"></div>
			<table id=\"eventpage\" summary=\"Players\">
				<tr>
					<th>Guests Players</th>
				</tr>
				<tr>
					<td><b>Women</b><br/>" . $PlayersWomen ."</td>
				</tr>
				<tr>
					<td><b>Men</b><br/>" . $Players ."</td>
				</tr>
				<tr>
					<td>&nbsp;</td>
				</tr>
			</table>
			";
	   }

      	  
	   if($npNumrows > 0 || $nonPlayMenSpouseRows > 0 || $nonPlayWomenSpouseRows > 0) {
	   	echo "
		   	<br/>
		   <b>Non-Players</b>";
	   }
	   
	   if($npNumrows > 0){
	   	echo "<table summary=\"Non-playing\">
	 					 <tr><td>Member</td></tr>";
	   	if($npNumrows > 0){
	   		$fgmembersite->outputNonPlayerInfo($npExtract, $EventID, $link, $url, $fgmembersite,$canAdd);
	   		echo "<tr><td>&nbsp;</td></tr>";
	   	}
	   	echo "</table>";
	   
	   }//end non-playing
	   
	   
	   //non playing spouses
	   if($nonPlayMenSpouseRows > 0 || $nonPlayWomenSpouseRows > 0){
	   	echo "<table summary=\"Non-playing-spouse\">
	 					 <tr><td >Spouse</td></tr>";
	   	if($spousePlayersnumrows == 0){
	   		$fgmembersite->outputNonPlayerInfo($nonPlayMenSpouse, $EventID, $link, $url, $fgmembersite, false);
	   	}
	   	if($spouseWomenPlayersRows == 0){
	   		$fgmembersite->outputNonPlayerInfo($nonPlayWomenSpouse, $EventID, $link, $url, $fgmembersite, false);
	   	}
	   	echo "<tr><td>&nbsp;</td></tr>";
	   	echo "</table>";
	   }
	   
	   if($isAdmin || $isCaptain)
	   {
	   	echo "<table><tr><td><b>Total Collected:&nbsp;</b></td><td class='totalCollected'></td></tr></table>";
	   }
	   
	   if ($Update3 != NULL)
		{
			echo "
					<div class=\"divider\"></div>
					 <div class='pull-left'  style='padding-bottom:8px'>
						<table id='bootstraptable' summary=\"Donations/Sponsorship\">
						<tr>
							<td style='padding-left:0px' colspan=2 class='title'>Donations/Sponsorship</td>
						</tr>
						<tr>
							<td>" . $Update3 ."</td>
						</tr>

					</table>
					</div>
					";
		}

		//display uploaded images
		$target_path = "images/past-events/". $id ."/";
		
		if ($GalleryLink != NULL)
		{
			$target_path = "gallery/$GalleryLink/";
		}
		include("mysql/carousel.php");
		
		

		echo "<div class='divider'></div>";


		if($canAdd){
			echo "<div class='col-md-12'>";
			echo "<p style='font-size:small'><i><span style='color:red'>**</span> Member is not current on dues and may be ineligible for match participation.</i></p>";
			echo "<p style='font-size:small'><span style='color:green' class='glyphicon glyphicon-ok' title='Paid Match Fee'></span> Member has paid the Match fee.</i></p>";
			echo "<p style='font-size:small'><span style='color:black' class='glyphicon glyphicon-ok' title='Paid Other Fee'></span> Member has paid an Additional/Optional Match fee.</i></p>";
			//echo "<p style='font-size:small'><span style='color:green' class='glyphicon glyphicon-thumbs-up' title='Approved By Captain'></span> Member was approved by Captain to play.</i></p>";
			echo "<p style='font-size:small;'><i>* Match payment not found.</i></p>";
			echo "</div>";
		}

	}//end id if


?>
<?php if(isset($_SESSION['mid'])) { ?>
<!-- Modal -->
  <div class="modal fade" id="myModal" role="dialog">
    <div class="modal-dialog">

      <!-- Modal content-->
      <div class="modal-content">
        <div class="modal-header">
          <button type="button" class="close" data-dismiss="modal">&times;</button>
          <h4 class="modal-title">YOUR SHOPPING CART</h4>
        </div>
        <div class="modal-body">
          <p id='pConfirm'></p>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-default" data-dismiss="modal" onclick="btnCheckout();">Checkout Now</button>
          <button type="button" class="btn btn-default" data-dismiss="modal" onclick="btnCart();">Modify Cart</button>
          <button type="button" class="btn btn-default" data-dismiss="modal" >Continue Shopping</button>
        </div>
      </div>

    </div>
  </div>

 
 <style>
 /* borderless table */
.table.table-borderless td, .table.table-borderless th {
    border: 0 !important;
}

.table.table-borderless {
    margin-bottom: 0px;
}
 </style>

<script type='text/javascript'>

	jQuery(document).ready(function() {
		$("#myCarousel").carousel();
		
		$('.btnPayFee').click(function() {
			var feeId = $("#selectFee").val();
			addCartItem(feeId);
	    });

		
		totalCollected();
	});

	function totalCollected()
	{
	  	var total = 0;
		$( ".feeAmountColl" ).each(function() {
			  var amountString = $( this ).html().replace("$", "");;
			  var number = Number(amountString.replace(/[^0-9\.]+/g,""));
			  total = total + number;

		});

		$( ".totalCollected" ).html(total.toLocaleString('en-US', { style: 'currency', currency: 'USD' }));
	}

	function btnCheckout()
	{
		window.location.href = "<?php echo  $this_url . "/member/fee/cart-checkout.php"?>";
	}

	function btnCart()
	{
		window.location.href = "<?php echo  $this_url . "/member/fee/cart.php"?>";
	}

	function addCartItem(feeId) {

		var mid = <?php echo htmlspecialchars($mid); ?>;
		jQuery.ajax({
			  url: "<?php echo  $this_url . "/mysql/addFeeToCart.php"?>" ,
			  type:"POST",
			  data:{feeId: feeId, mid: mid },
			  dataType: "json",
			  success: function(data){
				  if(data != ''){
					  $( "#pConfirm" ).html(data);
					  $('#myModal').modal('show');
 				  }
				  else
				  {
					  $( "#pConfirm" ).html("");
					  $('#myModal').modal('hide');
					  alert("There was an error adding the fee to the cart.");
				  }
			  }
			});

	}

	function nWin() {
		var w = window.open();
		w.document.title = 'USIC: Player Summary';
		var html = $("#tblConfirmed").html();

		$(w.document.body).html(html);
	}

	jQuery(function() {
		$("a#print").click(nWin);
	});

</script>

<?php } ?>
</div>
<?php include("includes/bootstrap_footer.html"); ?>
