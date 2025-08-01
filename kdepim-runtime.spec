#define git 20240217
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	K Desktop Environment Information Management runtime stuff
Name:		kdepim-runtime
Version:	25.04.3
Release:	%{?git:0.%{git}.}1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://community.kde.org/KDE_PIM
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/pim/kdepim-runtime/-/archive/%{gitbranch}/kdepim-runtime-%{gitbranchd}.tar.bz2#/kdepim-runtime-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/kdepim-runtime-%{version}.tar.xz
%endif
Patch0:		kdepim-runtime-23.03.90-clang-16.patch
BuildRequires:	boost-devel
BuildRequires:	sasl-devel
BuildRequires:	plasma6-akonadi
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KPim6GAPI)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6ItemModels)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6NotifyConfig)
BuildRequires:	cmake(KF6Codecs)
BuildRequires:	cmake(KF6Wallet)
BuildRequires:	cmake(KPim6Akonadi)
BuildRequires:	cmake(KPim6Mime)
BuildRequires:	cmake(KPim6AkonadiMime)
BuildRequires:	cmake(KPim6MailTransport)
BuildRequires:	cmake(KPim6IdentityManagementCore)
BuildRequires:	cmake(KPim6AkonadiContactCore)
BuildRequires:	cmake(KF6Contacts)
BuildRequires:	cmake(KF6CalendarCore)
BuildRequires:	cmake(KPim6CalendarUtils)
BuildRequires:	cmake(KPim6PimCommon)
BuildRequires:	cmake(KPim6IMAP)
BuildRequires:	cmake(KPim6AkonadiNotes)
BuildRequires:	cmake(KF6KCMUtils)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6Mbox)
BuildRequires:	cmake(KF6DAV)
BuildRequires:	cmake(KPim6Libkdepim)
BuildRequires:	cmake(KPim6LdapCore)
BuildRequires:	cmake(KPim6LdapWidgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineCore)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qca-qt6)
BuildRequires:	cmake(Qt6NetworkAuth)
BuildRequires:	cmake(Qt6Keychain)
BuildRequires:	cmake(KF6TextWidgets)
BuildRequires:	cmake(KF6TextTemplate)
BuildRequires:	shared-mime-info
BuildRequires:	xsltproc
Requires:	plasma6-akonadi >= %{version}
Requires:	plasma6-akonadi-contacts >= %{version}
%rename plasma6-kdepim-runtime
BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Information Management applications for the K Desktop Environment runtime libs.

#-----------------------------------------------------------------------------

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/kdepim-runtime.categories
%{_datadir}/qlogging-categories6/kdepim-runtime.renamecategories
%{_bindir}/*
%{_libdir}/qt6/plugins/kf6/kio/akonadi.so
#{_libdir}/qt6/plugins/kf6/kio/pop3.so
%{_datadir}/knotifications6/akonadi*
%{_datadir}/akonadi/agents/*.desktop
%{_datadir}/akonadi/davgroupware-providers
%{_datadir}/akonadi/firstrun/*
%{_datadir}/dbus-1/interfaces/org.kde.Akonadi.*.xml
%{_datadir}/icons/*/*/*/*.*
%{_datadir}/mime/packages/kdepim-mime.xml
%{_qtdir}/plugins/pim6/akonadi/config/*.so
%{_qtdir}/plugins/pim6/kcms/common/kcm_ldap.so
%{_datadir}/applications/org.kde.akonadi_davgroupware_resource.desktop
%{_datadir}/applications/org.kde.akonadi_google_resource.desktop
%{_datadir}/applications/org.kde.akonadi_imap_resource.desktop
%{_libdir}/qt6/plugins/pim6/mailtransport/mailtransport_akonadiplugin.so
%{_datadir}/applications/org.kde.akonadi_contacts_resource.desktop
%{_datadir}/applications/org.kde.akonadi_ews_resource.desktop
%{_datadir}/applications/org.kde.akonadi_openxchange_resource.desktop
%{_datadir}/applications/org.kde.akonadi_vcard_resource.desktop
%{_datadir}/applications/org.kde.akonadi_vcarddir_resource.desktop

%libpackage akonadi-filestore 6

%libpackage akonadi-singlefileresource 6

%libpackage folderarchivesettings 6

%libpackage kmindexreader 6

%libpackage maildir 6

%libpackage newmailnotifier 6
