<?php
    $returnURL = "/intmembers.html";
	include("mysql/checkuser.php");

	$searchFname = stripslashes($_GET['f']);

	$searchLname = stripslashes($_GET['l']);
?>

<?php include("includes/bootstrap_header.html"); ?>
<div class="container container-padding">
				<h1>IC Membership</h1>
				<img class="left noborder" src="images/join.jpg" alt="" height="130" width="130" />
				<p>
					Use the following links to find a list of IC members. <br />
					<br />
					You can search by:<br />
					(1) the first letter of the member's last name,
					(2) using the drop down list to see members by country,
					(3) or using the search boxes to find a string of letters in either the member's first or last name
				</p>
				<div class="text-center col-md-offset-1">
				<p>
					Find members by last name<br />
					<br />
					<a href="members.php?lastname=a">A</a>
					<a href="members.php?lastname=b">B</a>
					<a href="members.php?lastname=c">C</a>
					<a href="members.php?lastname=d">D</a>
					<a href="members.php?lastname=e">E</a>
					<a href="members.php?lastname=f">F</a>
					<a href="members.php?lastname=g">G</a>
					<a href="members.php?lastname=h">H</a>
					<a href="members.php?lastname=i">I</a>
					<a href="members.php?lastname=j">J</a>
					<a href="members.php?lastname=k">K</a>
					<a href="members.php?lastname=l">L</a>
					<a href="members.php?lastname=m">M</a>
					<a href="members.php?lastname=n">N</a>
					<a href="members.php?lastname=o">O</a>
					<a href="members.php?lastname=p">P</a>
					<a href="members.php?lastname=q">Q</a>
					<a href="members.php?lastname=r">R</a>
					<a href="members.php?lastname=s">S</a>
					<a href="members.php?lastname=t">T</a>
					<a href="members.php?lastname=u">U</a>
					<a href="members.php?lastname=v">V</a>
					<a href="members.php?lastname=w">W</a>
					<a href="members.php?lastname=x">X</a>
					<a href="members.php?lastname=y">Y</a>
					<a href="members.php?lastname=z">Z</a>
				</p>
				<div class='row'>
					Find members by Country<br />
					<form action="members.php" method="POST" class="form form-horizontal">
					 <div class="col-md-12 col-md-offset-4" >
           				<div class="col-md-3"  style='padding:0'>
						<select name="country" class='form-control'>
							<option value="Argentina">Argentina</option>
							<option value="Australia">Australia</option>
							<option value="Austria">Austria</option>
							<option value="Bahamas">Bahamas</option>
							<option value="Belgium">Belgium</option>
							<option value="Bermuda">Bermuda</option>
							<option value="Brazil">Brazil</option>
							<option value="Canada">Canada</option>
							<option value="Chile">Chile</option>
							<option value="Costa Rica">Costa Rica</option>
							<option value="Czech Republic">Czech Republic</option>
							<option value="Denmark">Denmark</option>
							<option value="France">France</option>
							<option value="Germany">Germany</option>
							<option value="Guatemala">Guatemala</option>
							<option value="Hungary">Hungary</option>
							<option value="India">India</option>
							<option value="Ireland">Ireland</option>
							<option value="Israel">Israel</option>
							<option value="Italy">Italy</option>
							<option value="Japan">Japan</option>
							<option value="Luxembourg">Luxembourg</option>
							<option value="Mexico">Mexico</option>
							<option value="Monaco">Monaco</option>
							<option value="Netherlands">Netherlands</option>
							<option value="New Zealand">New Zealand</option>
							<option value="Norway">Norway</option>
							<option value="Pakistan">Pakistan</option>
							<option value="Phillipines">Phillipines</option>
							<option value="Rhodesia">Rhodesia</option>
							<option value="Romania">Romania</option>
							<option value="Russia">Russia</option>
							<option value="Scotland">Scotland</option>
							<option value="South Africa">South Africa</option>
							<option value="Spain">Spain</option>
							<option value="Sweden">Sweden</option>
							<option value="Switzerland">Switzerland</option>
							<option value="United Kingdom">United Kingdom</option>
							<option value="Uruguay">Uruguay</option>
							<option value="Venezuela">Venezuela</option>
							<option value="Yugoslavia">Yugoslavia</option>
							</select>

						</div>
						<div class="col-md-1 pull-left" style='padding:0'>
							<input class='btn btn-usic' type='submit' name='submit' value='Search' />
						</div>
					  </div>
					</form>

				</div>
				<div style='padding-top:5px'>

					<form id="isearchNameFrm" name="isearchNameFrm" action="process.php" target="_self" method="post">

							<table style='border-spacing:2px;border-collapse:separate;margin:auto;padding:auto'>
							<tr>
								<td>First Name:</td>
								<td>Last Name:</td>
								<td></td>
							</tr>
							<tr>
								<td>
									<input class='form-control' type='text' name='FirstName' id='FirstName_form'/>
								</td>
								<td>
									<input class='form-control' type='text' name='LastName' id='LastName_form'/>
								</td>
								<td><div><input class='btn btn-usic' type='submit' name='submit' value='Search' /></div></td>
							</tr>
						</table>
						<input type="hidden" name="form" value="Int Name Search">
					</form>
				</div>
				<div style='padding-top:15px;padding-bottom:15px'>
				<?php
					//echo "<table id=\"event\" summary=\"Upcoming Events\">";

					//connect include
					require("mysql/connect-mysqli.php");

					//if the search is submitted show this
					//if ($_POST['submit'])
					if(!empty($searchFname) || !empty($searchLname))
					{
						$FirstName_form = $searchFname;
						$LastName_form = $searchLname;
						//$City_form = $_POST['City'];
						//$Country_form = $_POST['Country'];

						 $stmt = $link->prepare("SELECT MemberID, Email, LastName, FirstName, MiddleName, Suffix, Prefix, NickName FROM memberlist
							WHERE FirstName LIKE CONCAT('%', ?, '%')
						 	AND LastName LIKE CONCAT('%', ?, '%')
						 	AND Type = 'I'
						 	ORDER BY LastName ASC"
						 );

						$stmt->bind_param('ss', $FirstName_form, $LastName_form);

						$result = $stmt->execute();

						$stmt->bind_result($MemberID, $email, $LastName, $FirstName, $MiddleName, $Suffix, $Prefix, $Nickname);

						$stmt->store_result();

						$numrows = $stmt->num_rows;

						echo "<table id=\"bootstraptable\" class='table'>	";
						$z=0;
							echo "<tr>
									<th>Search Results</th>
									</tr>
									<tr>";
							if ($numrows == NULL)
							{
								echo"<td>No entries matched your search criteria. Please try again.</td>";
							}
							while($stmt->fetch())
							{

								echo "<td>";
								echo "<a href=\"member-info/" . $MemberID . "\">";
								echo $LastName;
								if ($Suffix != NULL)
								{
									echo " " . $Suffix;
								}
								echo ", " ;
								if ($Prefix != NULL)
								{
									echo $Prefix . " ";
								}
								echo $FirstName;
								if ($MiddleName != NULL)
								{
									echo " " . $MiddleName;
								}
								if ($Nickname != NULL)
								{
									echo " \"" . $Nickname . "\" ";
								}
								echo "</a>";
								echo "</td>";
								$z++;
									if ($z%3==0){
										echo "<tr/>";
										echo "<tr>";
									}

							}

							$stmt->close();

							echo "</tr>";
							echo"</table>";
					}


				?>

        </div>
        </div>

			</div><!-- end container -->
<?php include("includes/bootstrap_footer.html"); ?>
