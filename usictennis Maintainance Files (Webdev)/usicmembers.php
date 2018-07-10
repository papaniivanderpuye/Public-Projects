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
?>
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
	?>
	
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
		
		$stmt = $link->prepare ( "SELECT MemberID, Prefix, FirstName, MiddleName, LastName, Suffix , NickName FROM memberlist

		$result = $stmt->execute();
		$stmt->bind_result($MemberID, $Prefix, $FirstName, $MiddleName, $LastName, $Suffix, $Nickname);
		$stmt->store_result();
		$numrows = $stmt->num_rows;
		
		echo "<table class='table table-borderless' id=\"members\" summary=\"Members\">	";
		
		$z = 0;
		echo "<tr><th>Search Results</th></tr>
		
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

<?php include("includes/bootstrap_footer.html"); ?>