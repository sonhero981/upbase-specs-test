# Trích nguyên văn bốn bài trợ giúp TalentLMS

**Ngày lấy:** 07/10/2026 · **Người đưa:** PO

**Vì sao lưu ở đây:** `help.talentlms.com` chặn mọi lượt tải tự động *(Cloudflare, HTTP 403)*. Lấy được qua API Zendesk `https://help.talentlms.com/api/v2/help_center/en-us/articles/<id>.json`. Lưu lại để người sau không phải lấy lần nữa.

**Cách đọc:** chữ là nguyên văn, chỉ bỏ ảnh minh hoạ và số thứ tự chú thích ảnh. Phân tích nằm ở `working/ai-drafts/nghien-cuu-lms-khac-v0.2-20261007.md`.

---

## 1. How to use groups in branches in TalentLMS

**Nguồn:** https://help.talentlms.com/hc/en-us/articles/10730406045980-How-to-use-groups-in-branches-in-TalentLMS
**Bài cập nhật lần cuối:** 21/09/2026

In TalentLMS, you can organize your users into groups and branches according to your needs.
To learn more about groups and branches, as well as their differences, see this article.
The system also allows you to combine the two features by having groups within branches. Making a group part of a branch allows branch administrators to manage that group, including adding users, courses, and Learning Paths. This option would otherwise not be available for branch Administrators
A. Assigning groups to branches from the main domain:
1. Log in as an Administrator and create your group.
2. Once the group is created, click the Info tab. The Branch option is now available.
3. From the drop-down menu, select the branch this group will be assigned to.
4. Click Save to apply your changes.
Returning to the previous page, you can see the total list of groups you have in your portal. You can also identify which groups are assigned to which branches via the label with the branch name next to each group.
Note: If you need to unassign a group from a branch, click the Branch option followed by the select branch option from the drop-down menu. Click Update group to save your changes.
B. Branches and default groups:
If you have organized your training audience in different branches, TalentLMS lets you save time and effort by assigning a set of courses to all branch members at once using the branch default group.
1. Log in as an Administrator and go to Home > Branches.
2. Click to Edit a branch or create a new one.
3. Switch to the Info tab and scroll down to the Users section. On the Default group option, click Select a group for the drop-down menu to appear.
4. Select the group you want to assign as the default group of the branch.
5. Click Save to apply your changes.
Moving forward, each user created in the relevant branch will be added to the respective default group and enrolled in the group courses, provided that the courses are also assigned to the same branch.
Notes:

- A group can be set up as the default for more than one branch. However, each branch can have only one default group.

- The courses that belong to a group linked to a branch have to be assigned to the branch first.

C. Creating groups within the branch:
Apart from assigning existing groups to your branches, you can also create a group from scratch within a branch directly.
1. Log in as an Administrator and switch to a branch.
2. Go to Home > Groups and click Add group.
3. Type a Name and a Description for your group.
4. Add a Price if you are selling courses in bundles or create a Group key if you want users to self-register for a set of courses.
Note: If you'd like users added to this Group to be automatically enrolled in its training, enable Auto-enroll users to training.
5. Click Save to apply your changes.
6. After the new group has been added, you’re automatically taken to the Users tab on the group page. To add a user to your group, click Add user.
7. In the following drawer, search for the users you want to add to the group and click Enroll.
Note: If you have sent a group key to the users you want in the group, there’s no need to add them manually.
8. Go to the Courses tab to choose which courses the group members can access. To assign a course to your group, click Add course.
9. In the following drawer, search for the courses you want to add to the group and click Add.
10. Go to the Learning paths tab to assign Learning Paths to your group. Click Add learning path, search for the Learning Path you want, and click add it to the group.
11. Return to the Users tab to assign the selected courses to group members.

- To assign all courses to a specific user, hover over the respective user and click Add all remaining group courses to user.

- To remove all group courses from a specific user, hover over the respective user and click Remove all group courses from user.

Note: Group members aren't automatically enrolled in the Group's training when they're added manually by an Administrator or Instructor, even if the Group already contains courses or Learning Paths. To enroll existing members, use the available actions in the Users tab.
To enroll or unenroll all Group members in the Group's training at once, click Mass actions and choose the appropriate option.
Note: When users are unenrolled from a group’s Learning Path, they're also unenrolled from all courses included in that Learning Path. Their course progress and completion history are preserved, so if they're enrolled again later, they'll continue from where they left off.

---

## 2. How to share a file with all the users of a branch or group in TalentLMS

**Nguồn:** https://help.talentlms.com/hc/en-us/articles/9651458780444-How-to-share-a-file-with-all-the-users-of-a-branch-or-group-in-TalentLMS
**Bài cập nhật lần cuối:** 05/03/2026

TalentLMS lets you add files to a branch or a group and then make them available to all branch or group members directly through their profiles.
Here’s how to share a file with a branch or group members in a few steps:
1. Sign in to your TalentLMS account as an Administrator.
2. Click Groups or Branches and select the group or branch to which you want to add a file.
3. Click the Files tab and then the Upload files button.
4. Click the Select files to upload or drag and drop a file in that space. You can also specify an External URL to upload from.
Note: If you hover over the Select files to upload button, it will list the supported file types and sizes.
5. On your new file entry, in the Shared column, activate the shared option so the users can view that file.
If the group or branch already has files uploaded to them, the upload icon will be on the upper right side of your screen.
Note: You can upload more than one file at a time by using the Shift key to select them.
The file is now visible under My Files in the menu, which appears when you hover over your username. It will be accessible to users who are members of the branch or group where it is stored.

---

## 3. What is the Group Supervisor role in TalentLMS, and how it works

**Nguồn:** https://help.talentlms.com/hc/en-us/articles/27464091325340-What-is-the-Group-Supervisor-role-in-TalentLMS-and-how-it-works
**Bài cập nhật lần cuối:** 21/07/2026

The Group Supervisor role allows Admins or Group Owners to assign supervisory roles to group members, granting scoped access to group details and reports, and optionally messaging capabilities.
This role is useful when you need users with management or oversight responsibilities within the LMS.
Group Supervisors can monitor progress, coordinate and guide the learning journey of group participants, and communicate with users in the group.
The Group Supervisor is a functional role, similar to the Group Owner, and is different from the existing main user roles in TalentLMS (Administrator, Instructor, or Learner). It can be combined with a user’s existing role and permissions, depending on the access you want the user to have.
A Group Supervisor’s edit capabilities still depend on their underlying user type permissions (Administrator, Instructor, custom role, etc.).
Note: Group Supervisor functionality is available only in the new TalentLMS interface, and only in Pro and Enterprise plans. In the Pro plan, there is a limit of 10 groups max, including the main portal and branches. In the Enterprise plan, they are unlimited. The Group Supervisor isn’t supported on the legacy interface.
What can Group Supervisors access?

- They can view group details such as users, courses, files, and info. They can also access group reports from a dedicated Reports tab under their group, including overview, users, courses, and timeline, where they can view the report data, apply filters, and export the reports.

- They can contact group users if the relevant permission is enabled in Account & Settings > User types. For more info, see the Permissions section below.

- Group Supervisor permissions are scoped only to the assigned Groups. Multiple Group Supervisors can be assigned to one group independently, and one Supervisor can be assigned to multiple groups with scoped access per group.

Notes:

- Edit access depends on the user’s existing role. For example, users with Administrator or Instructor permissions may also have edit access to some group content.

- If a Group Supervisor (or a Group Owner) does not have an Admin-level role, they can only see shared group files. The uploader of the group files (e.g., an Admin) will need to switch the Share toggle on for the files in question to share them with the Group Supervisor.

How to make a user a Group Supervisor
A user can assign another user as a Group Supervisor if they have an Administrator-level role or are the Group Owner of the group and have the relevant group permissions (Groups > Update) enabled.
To assign a user as a Group Supervisor:
1. Sign in to your TalentLMS account as an Administrator, go to Groups, and open the group you wish to update.
2. Under the Users tab, hover over the user you wish to make the Group Supervisor and click the Make Supervisor icon that appears next to the user.
3. Confirm your choice.
The Group Supervisor is marked with a dedicated icon in the group’s user list.
To assign a user as a Group Supervisor:

- the user must already belong to the group.

- the user must have the Groups > Supervision > Supervise permission enabled in their user type.

This means that Group Supervisors do not necessarily need to be Administrators or Instructors.
You can also assign a Learner as a Supervisor by creating a custom user type that combines the Learner role with the additional Groups > Supervision > Supervise permission.
Notes:

- Users with a custom Learner + Supervise user type may need to switch to the corresponding Admin or Instructor role view in order to access supervised Groups.

- Group Supervisors are not automatically excluded from course or learning path enrollments assigned to the group.

- A Group Owner can also be assigned as a Group Supervisor.

Group Supervisor view
When you are the Group Supervisor of 1 or more groups, you can see the groups you supervise marked with a dedicated icon under the Groups menu of your portal.
How to remove Supervisor access
To remove Supervisor access:
1. Sign in to your TalentLMS account as an Administrator, go to Groups, and open the group you wish to update.
2. Under the Users tab, hover over the user you wish to remove the Supervisor access from, and click the Remove Supervisor icon that appears next to the user.
3. A confirmation pop-up will show up. Click Remove Supervisor once more to confirm.
When a user’s Supervisor access is removed, they will no longer be able to view the group’s details, access reports, or contact users in this group. Their existing user role permissions will remain unchanged.
Permissions (Group Supervision & Messaging)
The required user type permission for the Group Supervisor role is Groups > Supervision > Supervise.
This permission is available under both the Administrator and Instructor permission groups in user types.
Depending on where the permission is enabled, the user will access their supervised groups through the corresponding role context.

- Users with an Administrator-based user type and the Supervise permission enabled will access supervised groups through the Administrator interface.

- Users with an Instructor-based user type and the Supervise permission enabled will access supervised groups through the Instructor interface.

By default, group messaging permissions are disabled for Group Supervisors. If you'd like the Group Supervisor to message group users, enable the Groups > Supervision > Message group users permission.
Group Supervisors with this permission can message individual users or all users in the assigned group (except themselves), and recipients can reply to those messages.
Note: The Groups > Supervision > Supervise permission does not grant branch management access. If the Group Supervisor does not also have the Groups > Update permission, they cannot assign or unassign groups from branches.
Notifications
TalentLMS can automatically notify users when they are assigned as Group Supervisors through the Group Supervisor assignment notification event under System notifications.
This lets them know they now have Supervisor access to a specific group, including access to group details, reports, and messaging if enabled.

---

## 4. What happens if you delete a group or branch in TalentLMS?

**Nguồn:** https://help.talentlms.com/hc/en-us/articles/24882793526684-What-happens-if-you-delete-a-group-or-branch-in-TalentLMS
**Bài cập nhật lần cuối:** 01/09/2026

TalentLMS allows Administrators to delete Groups and Branches when they are no longer needed. Before proceeding, it’s important to understand how this action affects users, courses, and reporting.
Deleting a group or branch in TalentLMS is a permanent action and cannot be undone. This action does not delete users, courses, enrollments, or Learner progress.
Note: If you want to temporarily make a branch unavailable without permanently deleting it, you can deactivate it instead. To learn more, see What happens when you deactivate a branch in TalentLMS.
To delete a group or a branch:
1. Sign in to your TalentLMS account as an Administrator and navigate to Groups or Branches, depending on what you want to delete.
2. Locate the group or branch you want to remove and click Delete on the right side of the row.
3. Click Delete once more to confirm.
What happens after deletion?
A. Users
Users who were members of the deleted group or branch aren’t removed from the platform. They remain active and continue to exist in the main domain of your TalentLMS portal.
If the deleted branch was restricted (meaning its users did not have access to the main domain and were only able to sign in to that branch), its users will gain access to the main domain after the branch is deleted, provided they are not members of another restricted branch.
B. Courses and enrollments
If users were enrolled in courses through the deleted group or branch, those enrollments remain active. Course progress and completion data are preserved even after the group or branch has been deleted.
C. Courses created in a group or branch
Courses that were created within the deleted group or branch remain available. These courses continue to be available in the My training tab for users who are enrolled in them.
They will also be available in the Course catalog of the main domain, as long as they aren’t hidden.
Note: Deleting a group or branch in TalentLMS permanently removes the group or branch structure, while leaving users, courses, enrollments, and progress intact. The action is logged in the Timeline and can’t be reversed. For this reason, we recommend reviewing the impact carefully before proceeding with deleting groups or branches.

---
