***********************************
HyperDEX-0.1.0-alpha.8-Enhancements
***********************************

1. We have decided to remove the "Cancel" button from the Trades view. It was not working as expected and it doesn't look like it going to be possible to fix it until Marketmaker v2 (which will not be done soon). `Commit details <https://github.com/hyperdexapp/hyperdex/commit/60d9feecda1449222ac914f92e247b6e2cf54957>`_




2. Enable the EQL currency by default. Commit details

a. The Equaliser (EQL) coin is now a default active coin upon app install




3. Update to BarterDEX `Marketmaker v1.0.270 <https://github.com/artemii235/SuperNET/releases/tag/v1.0.270>`_ which contains a bug fix to improve order match rate.

a. Further details on this marketmaker update may be found here:

b. `Commit details <https://github.com/hyperdexapp/hyperdex/commit/74624bbdc8a01c55b366f7698542a33b57d1b5df>`_

c. `Marketmaker download <https://github.com/artemii235/SuperNET/releases>`_

4. Improve Content Security Policy `Commit details <https://github.com/hyperdexapp/hyperdex/commit/5d2751566ac8f305d9df5c5c214cf09bbe7e942a>`_

Add translation files Commit details
 
Correctly handle inverse values for sell orders. Commit details
Requested order values were displayed in reverse where the intended buy coin displayed as the intended sell coin. This has been corrected. More detailed information may be found here - https://github.com/hyperdexapp/hyperdex/issues/361

Add icons for currencies BCBC, MNZ, DNR, EQL Commit details
BCBC icon

MNZ icon

DNR icon

EQL icon


Split Settings into Portfolio and App Settings.
In the Settings view there are now two sections: Portfolio and App. To get to App settings select the Logout link or from the login page select Portfolio -> Settings




After either select the Logout link or selecting Portfolio -> Settings from the login page the App settings will be displayed allowing a custom market maker URL to be entered


Add some stats to the Trades view. Commit details
In the Trades -> Open Orders view a record of number of trades, number of currencies, and fiat value are now displayed in the top right corner



Fixes
Fix issue when clicking the "Max" button in the withdraw modal. Commit details
Fix stuck pending swaps. Commit details
Fix not being able to type space in the seed phrase input. Commit details
Fix USD calculation in the withdraw modal. Commit details
Fix problem with having currencies with a number in the name enabled.     Commit details

