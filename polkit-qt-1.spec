%define major 1

Name:		polkit-qt-1
Version:	0.103.0
Summary:	Library that allows developer to access PolicyKit-1 API
Release:	4
License:	LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://projects.kde.org/projects/kdesupport/polkit-qt-1
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2

BuildRequires:	polkit-1-devel >= 0.98.1
BuildRequires:	qt4-devel
BuildRequires:	cmake
BuildRequires:	automoc4

%description
Polkit-qt is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

#-----------------------------------------------------------------------------
%define libpolkit_qt_core_1 %mklibname polkit-qt-core-1_ %{major}

%package -n %{libpolkit_qt_core_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-core-10 < %{version}-%{release}

%description -n %{libpolkit_qt_core_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt_core_1}
%{_libdir}/libpolkit-qt-core-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt_gui_1 %mklibname polkit-qt-gui-1_ %{major}

%package -n %{libpolkit_qt_gui_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-gui-10 < %{version}-%{release}

%description -n %{libpolkit_qt_gui_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt_gui_1}
%{_libdir}/libpolkit-qt-gui-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt_agent_1 %mklibname polkit-qt-agent-1_ %{major}

%package -n %{libpolkit_qt_agent_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-agent-10 < %{version}-%{release}

%description -n %{libpolkit_qt_agent_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt_agent_1}
%{_libdir}/libpolkit-qt-agent-1.so.%{major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:	Devel stuff for polkit-Qt
Group:		Development/KDE and Qt
Requires:	%{libpolkit_qt_core_1} = %{version}-%{release}
Requires:	%{libpolkit_qt_gui_1} = %{version}-%{release}
Requires:	%{libpolkit_qt_agent_1} = %{version}-%{release}

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/polkit-qt-1
%{_libdir}/libpolkit-qt-agent-1.so
%{_libdir}/libpolkit-qt-core-1.so
%{_libdir}/libpolkit-qt-gui-1.so
%{_libdir}/pkgconfig/polkit-qt-1.pc
%{_libdir}/pkgconfig/polkit-qt-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt-core-1.pc
%{_libdir}/pkgconfig/polkit-qt-gui-1.pc
%{_libdir}/cmake/PolkitQt-1/*.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build


%changelog

