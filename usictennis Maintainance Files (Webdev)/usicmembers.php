<?php
$returnURL = "/usicmembers.php";

include ("mysql/checkuser.php");

include ("includes/bootstrap_header.html");

?>
<?php

$returnURL = "/usicmembers.php";
include ("mysql/checkuser.php");
$searchAge = stripslashes ( $_GET ['a'] );
$searchGender = stripslashes ( $_GET ['g'] );
$searchFname = stripslashes ( $_GET ['f'] );
$searchLname = stripslashes ( $_GET ['l'] );
$searchState = stripslashes ( $_GET ['state'] );
?><div class="container">	<h1>USIC Membership</h1>	<img class="left noborder" src="images/join.jpg" alt="" height="130"		width="130" />	<p style="line-height: 150%">		Use the following links to find a list of USIC members. <br /> <br />		There are two ways of searching for a member: by last name and by		state. For a last name search, click on the letter corresponding to		the first letter in the member's last name. For a geographic search,		enter the state and the person's name.	</p>	<br />	<div class="centered">		<p>			Find members by last name<br /> <br /> <a href="members.php?lname=a">A</a>			<a href="members.php?lname=b">B</a> <a href="members.php?lname=c">C</a>			<a href="members.php?lname=d">D</a> <a href="members.php?lname=e">E</a>			<a href="members.php?lname=f">F</a> <a href="members.php?lname=g">G</a>			<a href="members.php?lname=h">H</a> <a href="members.php?lname=i">I</a>			<a href="members.php?lname=j">J</a> <a href="members.php?lname=k">K</a>			<a href="members.php?lname=l">L</a> <a href="members.php?lname=m">M</a>			<a href="members.php?lname=n">N</a> <a href="members.php?lname=o">O</a>			<a href="members.php?lname=p">P</a> <a href="members.php?lname=q">Q</a>			<a href="members.php?lname=r">R</a> <a href="members.php?lname=s">S</a>			<a href="members.php?lname=t">T</a> <a href="members.php?lname=u">U</a>			<a href="members.php?lname=v">V</a> <a href="members.php?lname=w">W</a>			<a href="members.php?lname=x">X</a> <a href="members.php?lname=y">Y</a>			<a href="members.php?lname=z">Z</a>		</p>		<div class='row'>			Find members by state<br />			<!-- <form action="members.php" method="post"> -->			<form id="searchStFrm" name="searchStFrm" action="process.php"				target="_self" method="post">				<div class="col-md-12 col-md-offset-4">					<div class="col-md-3" style='padding: 0'>						<select name="state" size="1" class="st form-control">							<option value="AL">Alabama</option>							<option value="AK">Alaska</option>							<option value="AZ">Arizona</option>							<option value="AR">Arkansas</option>							<option value="CA">California</option>							<option value="CO">Colorado</option>							<option value="CT">Connecticut</option>							<option value="DE">Delaware</option>							<option value="DC">District of Columbia</option>							<option value="FL">Florida</option>							<option value="GA">Georgia</option>							<option value="HI">Hawaii</option>							<option value="ID">Idaho</option>							<option value="IL">Illinois</option>							<option value="IN">Indiana</option>							<option value="IA">Iowa</option>							<option value="KS">Kansas</option>							<option value="KY">Kentucky</option>							<option value="LA">Louisiana</option>							<option value="ME">Maine</option>							<option value="MD">Maryland</option>							<option value="MA">Massachusetts</option>							<option value="MI">Michigan</option>							<option value="MN">Minnesota</option>							<option value="MS">Mississippi</option>							<option value="MO">Missouri</option>							<option value="MT">Montana</option>							<option value="NE">Nebraska</option>							<option value="NV">Nevada</option>							<option value="NH">New Hampshire</option>							<option value="NJ">New Jersey</option>							<option value="NM">New Mexico</option>							<option value="NY">New York</option>							<option value="NC">North Carolina</option>							<option value="ND">North Dakota</option>							<option value="OH">Ohio</option>							<option value="OK">Oklahoma</option>							<option value="OR">Oregon</option>							<option value="PA">Pennsylvania</option>							<option value="RI">Rhode Island</option>							<option value="SC">South Carolina</option>							<option value="SD">South Dakota</option>							<option value="TN">Tennessee</option>							<option value="TX">Texas</option>							<option value="UT">Utah</option>							<option value="VT">Vermont</option>							<option value="VA">Virginia</option>							<option value="WA">Washington</option>							<option value="WV">West Virginia</option>							<option value="WI">Wisconsin</option>							<option value="WY">Wyoming</option>							<option value="INT">Members Living Abroad</option>						</select>					</div>					<div class="col-md-1 pull-left" style='padding: 0'>						<input class='btn btn-usic' type='submit' name='submit'	value='Search' />					</div>				</div>				<input type="hidden" name="form" value="State Search">			</form>		</div>	</div>	<div class="col-md-12">		<form id="searchNameFrm" name="searchNameFrm" action="process.php"	target="_self" method="post">			<table				style='border-spacing: 2px; border-collapse: separate; margin: auto; padding: auto'>				<tr>					<td>First Name:</td>					<td>Last Name:</td>					<td></td>				</tr>				<tr>					<td><input class='form-control' type='text' name='FirstName'						id='FirstName_form' /></td>					<td><input class='form-control' type='text' name='LastName'						id='LastName_form' /></td>					<td><div>							<input class='btn btn-usic' type='submit' name='submit'								value='Search' />						</div></td>				</tr>			</table>			<input type="hidden" name="form" value="Name Search">		</form>	</div>	<div>		<form id="searchAgeFrm" name="searchAgeFrm" action="process.php"			target="_self" method="post">			<div style="width: 100%">				<p class="centered">Find members by Age and Gender</p>				<table					style='border-spacing: 3px; border-collapse: separate; margin: auto; padding: auto'>					<tr>						<td>Age Range</td>						<td><select name="agerange" id="agerange">								<option value="20">20+</option>								<option value="25">25+</option>								<option value="30">30+</option>								<option value="35">35+</option>								<option value="40">40+</option>								<option value="45">45+</option>								<option value="50">50+</option>								<option value="50">55+</option>								<option value="60">60+</option>								<option value="65">65+</option>								<option value="70">70+</option>						</select></td>						<td>Gender</td>						<td><select name="gender" id="gender">								<option value="m">M</option>								<option value="f">F</option>						</select></td>						<td><input type='submit' name='submit' value='Search' /></td>								</table>			</div>			<input type="hidden" value="agerange" id="agerangeform"				name="agerangeform" /> <input type="hidden" name="form"				value="Age Search">		</form>	</div>
<?php

$previousSearch = false;

$previousNameSearch = false;

if (($searchAge != "") && $searchGender != "") 

{
	
	$previousSearch = true;
}

if ($searchFname != "" || $searchLname != "") {
	
	$previousNameSearch = true;
}

$agerangeform = stripslashes ( $_POST ['agerangeform'] );

if ($agerangeform == "agerange" || $previousSearch) 

{
	
	echo "<div id='srchDiv' class='divider'></div>";
	
	$gender = "";
	
	if ($previousSearch)
		
		$gender = $searchGender;
	
	else {
		
		$gender = stripslashes ( $_POST ['gender'] );
		
		if (strlen ( $gender ) > 1)
			
			$gender = substr ( $gender, 1 );
	}
	
	if ($previousSearch)
		
		$agerange = $searchAge;
	
	else {
		
		$agerange = stripslashes ( $_POST ['agerange'] );
		
		if (strlen ( $agerange ) > 2)
			
			$agerange = substr ( $agerange, 2 );
	}
	
	if (isset ( $_POST ['submit'] ) || $previousSearch) 

	{
		
		$startage = "";
		
		$endage = "";
		
		switch ($agerange) {
			
			case 20 :
				
				$startage = "20";
				
				$endage = "24";
				
				break;
			
			case 25 :
				
				$startage = "25";
				
				$endage = "29";
				
				break;
			
			case 30 :
				
				$startage = "30";
				
				$endage = "34";
				
				break;
			
			case 35 :
				
				$startage = "35";
				
				$endage = "39";
				
				break;
			
			case 40 :
				
				$startage = "40";
				
				$endage = "44";
				
				break;
			
			case 45 :
				
				$startage = "45";
				
				$endage = "49";
				
				break;
			
			case 50 :
				
				$startage = "50";
				
				$endage = "54";
				
				break;
			
			case 55 :
				
				$startage = "55";
				
				$endage = "59";
				
				break;
			
			case 60 :
				
				$startage = "60";
				
				$endage = "64";
				
				break;
			
			case 65 :
				
				$startage = "65";
				
				$endage = "69";
				
				break;
			
			case 70 :
				
				$startage = "70";
				
				$endage = "100";
				
				break;
		}
	}
	
	$extract = mysql_query ( "select * from (
								select CONCAT(City, ', ', State) as Address, firstname, lastname, dob, memberid, DATE_FORMAT(FROM_DAYS(TO_DAYS(NOW())-TO_DAYS(dob)), ' %y')+0 AS AGE
								from memberlist
								where dob is not null
								AND Type != 'I'
								AND Type != 'N'
								AND Type != 'P'
								AND Type != 'G'
								AND Type != 'IN'
								AND Type != 'DN'
								AND Type != 'T'
		 						AND Type != 'UK'
								AND Type != ''
								AND Gender = '$gender'
								) as agetable
								where AGE >='$startage' and AGE <='$endage'
								order by AGE
								" ) or die ( mysql_error () );
	
	$numrows = mysql_num_rows ( $extract );
	
	echo "<div class='col-md-6'><table class='table table-borderless' style='border-spacing:3px;border-collapse:separate'>
								<tr><th>Search Results: Age Range: " . $startage . "-" . $endage . " Gender:" . strtoupper ( $gender ) . "</th></tr>";
	
	while ( $row = mysql_fetch_assoc ( $extract ) ) 
	{
		
		$MemberID = $row ['memberid'];
		
		$age = $row ['AGE'];
		
		$FirstName = $row ['firstname'];
		
		$LastName = $row ['lastname'];
		
		$DOB = $row ['DOB'];
		
		$Addr = $row ['Address'];
		
		echo "<tr>";
		
		echo "<td class='text-left'>";
		
		echo "<a href=\"member-info/" . $MemberID . "/a/" . $agerange . "/g/" . $gender . "\">";
		
		echo $LastName;
		
		if ($Suffix != NULL){
			
			echo " " . $Suffix;
		}
		
		echo ", ";
		
		
		
		echo $FirstName;
		
		if ($MiddleName != NULL) {
			
			echo " " . $MiddleName;
		}
		
		if ($Nickname != NULL) {
			
			echo " \"" . $Nickname . "\" ";
		}
		
		echo "</a>";
		
		if (trim ( $Addr ) == ",")
			
			$Addr = "";
		
		echo " " . $Addr . " Age: " . $age;
		
		echo "</td>";
		
		echo "</tr>";
	} // end while
	echo "</table></div>";
} 

else {
	echo "</div>";
	
	// echo "</div>";
	// echo "</div>";
	// echo "</div>";
	?><?php
	
	// echo "<table class='table table-borderless' id=\"event\" summary=\"Members\">";
	require("mysql/connect-mysqli.php");
	// if the search is submitted show this
	
	if ($_POST ['submit'] || $previousNameSearch) {
		
		if ($previousNameSearch && ! empty ( $searchFname ))
			$FirstName_form = $searchFname;
		else
			$FirstName_form = trim ( stripslashes ( $_POST ['FirstName'] ) );
		
		if ($previousNameSearch && ! empty ( $searchLname ))
			$LastName_form = $searchLname;
		else
			$LastName_form = trim ( stripslashes ( $_POST ['LastName'] ) );
		
		$City_form = trim ( stripslashes ( $_POST ['City'] ) );
		
		$Country_form = trim ( stripslashes ( $_POST ['Country'] ) );
		
		if (strlen ( $FirstName_form ) > 10)			
			$FirstName_form = substr ( $FirstName_form, 10 );
		
		if (strlen ( $City_form ) > 10)			
			$City_form = substr ( $City_form, 10 );
		
		if (strlen ( $LastName_form ) > 10)			
			$LastName_form = substr ( $LastName_form, 10 );
		
		if (strlen ( $Country_form ) > 15)			
			$Country_form = substr ( $Country_form, 15 );
		
		$stmt = $link->prepare ( "SELECT MemberID, Prefix, FirstName, MiddleName, LastName, Suffix , NickName FROM memberlist							WHERE FirstName LIKE '%$FirstName_form%'							AND LastName LIKE '%$LastName_form%'							And Type != 'I'							And Type != 'P'							And Type != 'N'							AND Type != 'IN'							AND Type != 'DN'							AND Type != 'T'							AND Type != 'UK'							AND Type != ''							ORDER BY LastName ASC" );

		$result = $stmt->execute();
		$stmt->bind_result($MemberID, $Prefix, $FirstName, $MiddleName, $LastName, $Suffix, $Nickname);
		$stmt->store_result();
		$numrows = $stmt->num_rows;
		
		echo "<table class='table table-borderless' id=\"members\" summary=\"Members\">	";
		
		$z = 0;
		echo "<tr><th>Search Results</th></tr>							<tr>";
		
		if ($numrows == NULL) 
		{			
			echo "<td>No entries matched your search criteria. Please try again.</td>";
		}
		
		while ( $stmt->fetch() ) {
			
			
			echo "<td>";
			
			if (! empty ( $LastName_form ))
				
				echo "<a href=\"member-info/" . $MemberID . "/l/" . $LastName_form . "\">";
			
			else if (! empty ( $FirstName_form ))
				
				echo "<a href=\"member-info/" . $MemberID . "/f/" . $FirstName_form . "\">";
			
			else
				
				echo "<a href=\"member-info/" . $MemberID . "\">";
			
			echo $LastName;
			
			if ($Suffix != NULL){
				
				echo " " . $Suffix;
			}
			
			echo ", ";
			
			
			echo $FirstName;
			
			if ($MiddleName != NULL){
				
				echo " " . $MiddleName;
			}
			
			if ($Nickname != NULL){
				
				echo " \"" . $Nickname . "\" ";
			}
			
			echo "</a>";
			
			echo "</td>";
			
			$z ++;
			
			if ($z % 1 == 0){
				
				echo "</tr>";
				
				echo "<tr>";
			}
		} // end while
		
		echo "</tr>";
		
		echo "</table>";
	} // end if
}

?>
	<script type="text/javascript">		$( document ).ready(function() {		 	var myParam = location.search.split('state=')[1];		 	var anyParam = location.search.split('?')[1];		 	if(myParam != "")		 	{		 		$('.st option[value=' + myParam +']').attr('selected','selected');		 	}		 	if(myParam != ""){		 		document.getElementById('srchDiv').scrollIntoView();			}		});	</script>
<?php include("includes/bootstrap_footer.html"); ?>
