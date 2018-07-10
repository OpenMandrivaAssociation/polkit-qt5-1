%define major 1
%define	oname polkit-qt-1

Summary:	Library that allows developer to access PolicyKit-1 API
Name:		polkit-qt5-1
Version:	0.112.0
Release:	8
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/kdesupport/polkit-qt-1
Source0:	http://mirrors.dotsrc.org/kde/stable/apps/KDE4.x/admin/%{oname}-%{version}.tar.bz2
# From upstream git (git://anongit.kde.org/polkit-qt-1.git)
Patch0:		0001-do-not-use-global-static-systembus-instance.patch
Patch1:		0002-fix-build-with-Qt4-which-doesn-t-have-QStringLiteral.patch
Patch2:		0003-Fix-QDBusArgument-assertion.patch
Patch3:		0004-Add-.reviewboardrc.patch
Patch4:		0005-Add-wrapper-for-polkit_system_bus_name_get_user_sync.patch
Patch5:		0006-Drop-use-of-deprecated-Qt-functions.patch
# 0007-Fix-compilation-with-Qt5.6.patch intentionally excluded (not needed with current compilers)
Patch7:		0008-Allow-compilation-with-older-polkit-versions.patch
Patch8:		0009-Fix-build-with-DBUILD_TEST-TRUE.patch
Patch9:		0010-polkitqtlistener.cpp-pedantic.patch
Patch10:	0011-Remove-unused-file.patch
Patch11:	0012-Add-.arcconfig.patch
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	qt5-devel >= 5.1.0
BuildRequires:	pkgconfig(polkit-agent-1)
# To make qmake happy
BuildRequires:	qt5-platformtheme-gtk3

%description
Polkit-qt is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

#-----------------------------------------------------------------------------
%define libpolkit_qt5_core_1 %mklibname polkit-qt5-core-1_ %{major}

%package -n %{libpolkit_qt5_core_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Provides:	polkit-agent

%description -n %{libpolkit_qt5_core_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt5_core_1}
%{_libdir}/libpolkit-qt5-core-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt5_gui_1 %mklibname polkit-qt5-gui-1_ %{major}

%package -n %{libpolkit_qt5_gui_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries

%description -n %{libpolkit_qt5_gui_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt5_gui_1}
%{_libdir}/libpolkit-qt5-gui-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt5_agent_1 %mklibname polkit-qt5-agent-1_ %{major}

%package -n %{libpolkit_qt5_agent_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries

%description -n %{libpolkit_qt5_agent_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt5_agent_1}
%{_libdir}/libpolkit-qt5-agent-1.so.%{major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:	Devel stuff for polkit-Qt
Group:		Development/KDE and Qt
Requires:	%{libpolkit_qt5_core_1} = %{version}-%{release}
Requires:	%{libpolkit_qt5_gui_1} = %{version}-%{release}
Requires:	%{libpolkit_qt5_agent_1} = %{version}-%{release}

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/polkit-qt5-1
%{_libdir}/libpolkit-qt5-agent-1.so
%{_libdir}/libpolkit-qt5-core-1.so
%{_libdir}/libpolkit-qt5-gui-1.so
%{_libdir}/pkgconfig/polkit-qt5-1.pc
%{_libdir}/pkgconfig/polkit-qt5-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt5-core-1.pc
%{_libdir}/pkgconfig/polkit-qt5-gui-1.pc
%{_libdir}/cmake/PolkitQt5-1/*.cmake

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{oname}-%{version}

%build
%cmake_qt5 -DBUILD_EXAMPLES:BOOL=OFF -G Ninja
%ninja_build

%install
%ninja_install -C build
