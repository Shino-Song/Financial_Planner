# Financial_Planner
Open source financial planning software

# Introduction

Hello! To give the simplest introduction, this is a personal project that I am making for the purpose of using myself. The goal is to build a financial planner that can track financial data dynamically, give simple and detailed overviews, intelegently manage budgets and goals, and intelegently ingest bank/credit card documentation then sort the information to its appropriate destination.

This is also my first major project I am starting for the prupose of practical use. There is definitely a lot I will be learning and as such, the state of the project will likely change dramatically over time. I do not plan to feature creep the project unless it is a feature that is necessary to make other aspects work. Any new non-critical features will be made low priority until existing planned features are in an acceptable state. Followers of the project are welcome to leave suggestions and for their own branch for development given you provide appropriate attribution of the original development.

# General expectations of use (to be replaced by license eventually)

At this time (and this will be edited out when no longer applicable), there is no set license. I am looking at the options for what is most appropriate for my goals in this project. So until then, understand that this project is inherently intended to be free and open source. Those who wish to use it or make your own fork of it may at any point so long as you make some notable reference back to the original (eg. "Powered by (insert whatever I end up calling this software here)"). While the software is free, if you wish to include it in a suite or as the foundation of something you make and charge a fee for, that is fine, but understand that I am not responsible or liable for any issues or losses you may face while offering this software to your customers. For that, you may make a note of an issue that you have found and I will get to it when I get to it, else you are welcome to attempt to fix it in your own fork (TL;DR - Your customers aren't paying me to fix the problems, so don't whine about your losses to me unless you'd like to help fund it). And finally, while I promise to never lock, delete, or otherwise intentionaly destroy the functionality of this software, I cannot and will not guarantee the stability, functionality, or continued development of this software. If something is changed that you didn't want changed, let me know kindly and I will take it into honest consideration. If something broke, go back to the last version where it worked and let me know so I can attempt to fix it. If I fall off the face of this universe, I will attempt to make a post about it beforehand, but otherwise I will do everything I can to make sure the repo is as eternal as GitHub allows and permit others to fork it for continued development.

# Features/to-do

Here is a list of the planned features of the software. This will be updated periodically to indicate new features, refine the current listings, the priority of the features, and what the current status of the features are.

Priority key:

H = High priority, the most important of general development.
L = Low priority, it is going to happen, but takes a back seat to other features.
! = Critical, everything else is on pause until this is fixed. Do not expect to see this often, as critical tasks should be done before I even think about updating the list (unless there is something very important that I need to inform everyone about)

1: Actual balance (H) - This is a field that displays your actual balance and is manually inputted.
2: Calculated balance (H) - This is a field that takes the actual balance of the previous month and the math of income and expenses to display what the actual balance should be.
3: Actual/Calculated balance agreement indication (H) - States if the Actual and Calculated balances are in agreement or disagreement to indicate if there is a clerical error in the data entry.
4: Total etsimated/actual income (H) - Fields that take projected and actual gross/net income reports to show what you can expect to have in an requested time period. Can take multiple sounces of income fields to keep track of different income sources.
5: Total estimated/actual income agreement indication (H) - This compares the total actual and estimated incomes and individual income sources to determine trends of what you estimated and actually recieved.
6: Deductions estimation (H) - a preset calculation to run various deducations from the Total estimated/actual income entries (eg. taxes, insurance, etc...). This should be items that are taken out of the Gross income before it hits your bank account or an amount that should be set aside if items are not automatically deducted.
7: Categorized expenses (H) - Separate customizable sections of expense types (eg. utilities, food, phone/internet/, fun, etc...). This is further broken down into indivudual expenses that can be projected, manually added, or automatically pulled from bank/credit card statements and organized locally (never sent off of your computer).
8: Bank/credit card statement organization (L) - A system that reads income/expense reports from your bank and credit card statements and automatically sorts them into the appropriate categories with time stamps and details as provided.
9: Savings planner (L) - A tool to create a dynamic budgeting plan for a savings goal.
10: Bank integration (L) - A tool that can integrate with your bank/credit card to automatically pull data and update the relevant fields at set intervals (will never send data out to other places. Low priority until I know how to ensure the highest level privacy).

# Closing statement

As I have mentiond, this is more of a project for myself and what I would like to have for my own uses. It is something I would find useful to enrich my own life and be useful as a project to better learn programming. I can foresee many concerns and roadblocks along the way, from maintaining privacy to ramming my head against a wall on how to implement a feature. I am also by no means an artist of any kind, so making the front end visually appealing is something I will be working on and likely outsource if I find support for the project. This project is not to fill a niche or cause an upset in the market, in fact, I haven't even looked at what professional offerings there are! This is not intended to be used for any critical or high stakes environments, especially in ways that are mission critical as if there is a problem with the software, I make no guarantees to anything, let alone any claim of quality. I am also not without my own self interest, while I have promised and will continue to promise that the software is open and free, I will likely give options to help support and encourage my project through monetary means (the sooner I have my annoying student debts eleminated, the happier this dev will be!). Any and all forms of support will strictly be voluntary and have no impact on feature priorities or timeline estimates unless you want to throw me lifechanging amounts of support. For 4 or more figures, I will happily prioritize a feature or fix, but no amount of money will change the fact this will be forever an open and free project.

I hope you who have stumbled upon this project and read this far have taken interest in the ramblings of this madman and enjoy following the progress of whatever adventure this project becomes! Who knows, maybe I'll even start streaming it at some point ㅋㅋㅋ

Signing off,
Shino
