%define major 1
%define	oname polkit-qt-1

Summary:	Library that allows developer to access PolicyKit-1 API
Name:		polkit-qt5-1
Version:	0.113.0
Release:	2
License:	LGPLv2+
Group:		Graphical desktop/KDE
Url:		https://projects.kde.org/projects/kdesupport/polkit-qt-1
Source0:	http://download.kde.org/stable/polkit-qt-1/%{oname}-%{version}.tar.xz
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
